from fastapi import APIRouter
from typing import List
from ..models.operations import Operation
from ..database import Session
from .. import tables
router = APIRouter(
    prefix='/operations'
)


@router.get('/', response_model=List[Operation])
def get_operations():
    session = Session()
    operations = (
        session
        .query(tables.Operation)
        .all())
    return operations