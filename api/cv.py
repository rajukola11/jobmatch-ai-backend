from fastapi import APIRouter
from models.cv import CVRequest
from services.cv_service import generate_cv_logic

router = APIRouter()

@router.post("/generate-cv")
async def generate_cv(data: CVRequest):
    return {
        "tailored_cv": generate_cv_logic(data.job_description, data.base_cv)
    }