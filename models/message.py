from pydantic import BaseModel
from typing import Optional

class MessageRequest(BaseModel):
    job_description: str
    company: str
    recipient_name: Optional[str] = ""