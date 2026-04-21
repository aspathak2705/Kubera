from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.services.loan_service import create_loan_application
from app.models.loan_application import LoanApplication

router = APIRouter(prefix="/loans", tags=["Loans"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/apply")
def apply_loan(
    name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
    income: float = Form(...),
    employment_status: str = Form(...),
    credit_score: int = Form(None),

    amount: float = Form(...),
    purpose: str = Form(...),
    tenure: int = Form(...),

    id_document: UploadFile = File(...),
    income_proof: UploadFile = File(...),
    bank_statement: UploadFile = File(...),

    db: Session = Depends(get_db)
):
    try:
        data = {
            "applicant": {
                "name": name,
                "email": email,
                "phone": phone,
                "income": income,
                "employment_status": employment_status,
                "credit_score": credit_score
            },
            "loan": {
                "amount": amount,
                "purpose": purpose,
                "tenure": tenure
            }
        }

        files = {
            "id_document": id_document,
            "income_proof": income_proof,
            "bank_statement": bank_statement
        }

        loan = create_loan_application(data, files, db)

        return {
            "success": True,
            "application_id": loan.id
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/status/{id}")
def check_status(id: int, db: Session = Depends(get_db)):
    loan = db.query(LoanApplication).filter(LoanApplication.id == id).first()

    if not loan:
        raise HTTPException(status_code=404, detail="Application not found")

    return {
        "application_id": loan.id,
        "status": loan.status
    }