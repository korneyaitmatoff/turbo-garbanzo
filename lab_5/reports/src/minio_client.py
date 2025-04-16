from minio import Minio

from src.config import (
    S3_HOST,
    S3_PORT,
    ACCESS_KEY,
    SECRET_KEY
)

client = Minio(
    endpoint=f"{S3_HOST}:{S3_PORT}",
    access_key=ACCESS_KEY,
    secret_key=SECRET_KEY,
    secure=False
)


def load_report(object_name: str, filepath: str):
    if client.bucket_exists(bucket_name="reports") is False:
        client.make_bucket(
            bucket_name="reports"
        )

    client.fput_object(
        bucket_name="reports",
        object_name=object_name,
        file_path=filepath
    )
