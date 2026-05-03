from fastapi import APIRouter, HTTPException
from models.cv import CVRequest
from services.cv_service import generate_cv_logic

router = APIRouter()

@router.post("/generate-cv")
async def generate_cv(data: CVRequest):
    try:
        result = generate_cv_logic(data.job_description, data.base_cv)
        return {"tailored_cv": result}
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))