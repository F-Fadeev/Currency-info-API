import uvicorn
from fastapi import FastAPI

from source.api.router import router
from source.tasks.router import celery_router

app = FastAPI()
app.include_router(router)
app.include_router(celery_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)



