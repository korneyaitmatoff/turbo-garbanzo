from requests import Session

from src.config import (
    API_HOST,
    API_PORT
)


def get_all_data():
    session = Session()

    response = session.get(
        url=f"http://{API_HOST}:{API_PORT}/"
    )

    return response.json()

