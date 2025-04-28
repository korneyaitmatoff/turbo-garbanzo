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


def get_report_from_s3(object_name: str, filepath: str):
    client.fget_object(
        bucket_name="reports",
        object_name=object_name,
        file_path=filepath
    )