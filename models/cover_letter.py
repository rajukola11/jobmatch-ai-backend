from pydantic import BaseModel

class CoverLetterRequest(BaseModel):
    job_description: str
    company: str
    base_cv: str