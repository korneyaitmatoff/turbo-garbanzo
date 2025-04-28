from typing import TypedDict

from psycopg2 import connect
from psycopg2.extras import RealDictCursor

from src.config import (
    POSTGRES_USER,
    POSTGRES_PASSWORD,
    POSTGRES_DB,
    DB_HOST,
    DB_PORT
)
from src.models import Car

connection = connect(
    dsn=f"postgres://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DB_HOST}:{DB_PORT}/{POSTGRES_DB}"
)


def select_all():
    cursor = connection.cursor(cursor_factory=RealDictCursor)
    cursor.execute(
        query="SELECT * FROM cars;"
    )
    data = cursor.fetchall()
    cursor.close()
    return data


def insert(data: Car):
    cursor = connection.cursor(cursor_factory=RealDictCursor)
    cursor.execute(
        query=f"INSERT INTO cars(name, cost, is_writeoff, is_rented) "
              f"values ('{data.name}', {data.cost}, {data.is_writeoff}, {data.is_rented})"
    )
    cursor.connection.commit()


def select_by_uuid(uuid: str):
    cursor = connection.cursor(cursor_factory=RealDictCursor)
    cursor.execute(
        query=f"SELECT * FROM cars where id = '{uuid}';"
    )
    data = cursor.fetchall()
    cursor.close()
    return data


def update(
        uuid: str,
        data: Car
):
    query = f"UPDATE cars SET "

    for attr in data.model_fields:
        if getattr(data, attr) is not None:
            if isinstance(getattr(data, attr), str):
                query += f"{attr}='{getattr(data, attr)}',"
            else:
                query += f"{attr}={getattr(data, attr)},"

    query = query[:-1] + f" WHERE id = '{uuid}'"

    cursor = connection.cursor(cursor_factory=RealDictCursor)
    cursor.execute(
        query=query
    )
    cursor.connection.commit()
    cursor.close()


def delete_by_uuid(uuid: str):
    cursor = connection.cursor(cursor_factory=RealDictCursor)
    cursor.execute(
        query=f"DELETE FROM cars where id = '{uuid}'"
    )
    cursor.connection.commit()

    cursor.close()
