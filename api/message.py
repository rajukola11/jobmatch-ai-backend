from fastapi import APIRouter
from models.message import MessageRequest
from services.message_service import generate_message_logic

router = APIRouter()

@router.post("/generate-message")
async def generate_message(data: MessageRequest):
    return {
        "message": generate_message_logic(data.job_description, data.company)
    }