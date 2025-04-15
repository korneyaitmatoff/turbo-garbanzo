from pydantic import BaseModel


class Car(BaseModel):
    name: str | None = None
    cost: float | None = None
    is_writeoff: bool | None = None
    is_rented: bool | None = None
