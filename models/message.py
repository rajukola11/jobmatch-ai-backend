from pydantic import BaseModel

class MessageRequest(BaseModel):
    job_description: str
    company: str