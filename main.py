from fastapi import FastAPI
from api import job, cv, message
from api.cover_letter import router as cover_letter_router


app = FastAPI()

app.include_router(job.router)
app.include_router(cv.router)
app.include_router(message.router)
app.include_router(cover_letter_router)