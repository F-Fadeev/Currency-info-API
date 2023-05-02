from fastapi import APIRouter, status

from source.api.schemas import Currency
from source.db.database import get_database

router = APIRouter(tags=["Currency"])

client = get_database()
db = client["BTC-rates"]


@router.get(
    "/",
    response_model=list[Currency],
    status_code=status.HTTP_200_OK
)
def get_all_data():
    all_data = []
    for data in db.find():
        data["_id"] = str(data["_id"])
        all_data.append(data)
    return all_data
