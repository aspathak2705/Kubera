from pydantic import BaseModel

class ApplicantCreate(BaseModel):
    name: str
    email: str
    phone: str
    income: float
    employment_status: str
    credit_score: int | None
    