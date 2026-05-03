from fastapi import APIRouter, HTTPException
from models.message import MessageRequest
from services.message_service import generate_message_logic

router = APIRouter()

@router.post("/generate-message")
async def generate_message(data: MessageRequest):
    try:
        result = generate_message_logic(data.job_description, data.company, data.recipient_name)
        return {"message": result}
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))