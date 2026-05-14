from pydantic import BaseModel

class PDFRequest(BaseModel):
    job_title: str
    company: str
    tailored_cv: str
    cover_letter: str
    message: str