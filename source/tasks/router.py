from fastapi import APIRouter

from source.tasks.task import get_currency_task

celery_router = APIRouter(prefix="/report", tags=["Report"])


@celery_router.get("/dashboard")
def get_report():
    get_currency_task.delay()
    return {"message": "OK"}
