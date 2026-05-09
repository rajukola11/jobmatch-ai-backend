from pydantic import BaseModel

class CVRequest(BaseModel):
    job_description: str
    cv_text: str