from fastapi import APIRouter
from models.cover_letter import CoverLetterRequest
from services.cover_letter_service import generate_cover_letter_logic

router = APIRouter()

@router.post("/generate-cover-letter")
async def generate_cover_letter(data: CoverLetterRequest):
    return {
        "cover_letter": generate_cover_letter_logic(
            data.job_description,
            data.company,
            data.base_cv
        )
    }