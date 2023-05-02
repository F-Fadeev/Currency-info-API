from datetime import datetime, timedelta

from celery import Celery
import requests

from source.db.database import get_database


celery_app = Celery(
    "my_celery",
    broker="redis://localhost:6379",
)


client = get_database()
db = client["BTC-rates"]


@celery_app.task
def get_currency_task():
    response = requests.get("https://blockchain.info/ticker")
    if response.status_code == 200:
        data = response.json()
        rates = {currency: data[currency]['last'] for currency in data}
        rates['date'] = datetime.now()
        db.insert_one(rates)

