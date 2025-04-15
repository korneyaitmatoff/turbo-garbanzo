from typing import Any


def prepare_report(data: list[dict[str, Any]]) -> dict[str, int]:
    is_writeoff_count = 0
    is_rented_count = 0
    is_not_rented_count = 0

    for item in data:
        if item["is_writeoff"] is True: is_writeoff_count += 1
        if item["is_rented"] is True: is_rented_count += 1
        if item["is_rented"] is False: is_not_rented_count += 1

    return {
        "is_writeoff_count": is_writeoff_count,
        "is_rented_count": is_rented_count,
        "is_not_rented_count": is_not_rented_count
    }
