from pydantic import BaseModel

class CVRequest(BaseModel):
    job_description: str
    base_cv: str