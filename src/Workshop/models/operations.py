from pydantic import BaseModel
from datetime import date
from decimal import Decimal
from enum import Enum
from typing import Optional


class Operationkind(str, Enum):
    INCOME = "income"
    OUTCOME = "outcome"


class Operation(BaseModel):
    id: int
    data: date
    kind: Operationkind
    amount: Decimal
    description: Optional[str]

    class Config:
        orm_mode = True
