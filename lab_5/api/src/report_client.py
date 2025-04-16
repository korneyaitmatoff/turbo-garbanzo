from requests import Session

from src.config import (
    REPORT_HOST,
    REPORT_PORT
)


def get_report():
    session = Session()

    response = session.get(
        url=f"http://{REPORT_HOST}:{REPORT_PORT}/report"
    )

    return response.json()
