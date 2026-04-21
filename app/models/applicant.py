from sqlalchemy import Column, Integer, String, Float
from app.db import Base

class Applicant(Base):
    __tablename__ = "applicants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)

    income = Column(Float, nullable=False)
    employment_status = Column(String, nullable=False)
    credit_score = Column(Integer, nullable=True)