from datetime import datetime

from bson import ObjectId
from pydantic import BaseModel, Field


class Currency(BaseModel):
    _id: ObjectId = Field(alias="_id")
    ARS: float
    AUD: int
    BRL: float
    CAD: float
    CHF: float
    CLP: float
    CNY: float
    CZK: float
    DKK: float
    EUR: float
    GBP: float
    HKD: float
    HRK: float
    HUF: float
    INR: float
    ISK: float
    JPY: float
    KRW: float
    NZD: float
    PLN: float
    RON: float
    RUB: float
    SEK: float
    SGD: float
    THB: float
    TRY: float
    TWD: float
    USD: float
    date: datetime
