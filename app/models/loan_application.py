from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db import Base

class LoanApplication(Base):
    __tablename__ = "loan_applications"

    id = Column(Integer, primary_key=True, index=True)

    applicant_id = Column(Integer, ForeignKey("applicants.id"))

    amount = Column(Float, nullable=False)
    purpose = Column(String, nullable=False)
    tenure = Column(Integer, nullable=False)

    status = Column(String, default="PENDING")

    id_document = Column(String)
    income_proof = Column(String)
    bank_statement = Column(String)

    applicant = relationship("Applicant")