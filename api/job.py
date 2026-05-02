from fastapi import APIRouter
from models.job import JobRequest
from services.job_service import analyze_job_logic

router = APIRouter()

@router.post("/analyze-job")
async def analyze_job(data: JobRequest):
    return analyze_job_logic(data.job_description)