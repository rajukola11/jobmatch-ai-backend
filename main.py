from fastapi import FastAPI
from api import job, cv, message

app = FastAPI()

app.include_router(job.router)
app.include_router(cv.router)
app.include_router(message.router)