from sqlalchemy.orm import Session
from app.models.applicant import Applicant
from app.models.loan_application import LoanApplication
from app.services.file_service import save_file

def create_loan_application(data, files, db: Session):

    try:
        # Step 1: Create applicant
        applicant = Applicant(**data["applicant"])
        db.add(applicant)
        db.commit()
        db.refresh(applicant)

        # Step 2: Save files
        id_path = save_file(files["id_document"], "uploads/id_documents")
        income_path = save_file(files["income_proof"], "uploads/income_proofs")
        bank_path = save_file(files["bank_statement"], "uploads/bank_statements")

        # Step 3: Create loan
        loan = LoanApplication(
            applicant_id=applicant.id,
            amount=data["loan"]["amount"],
            purpose=data["loan"]["purpose"],
            tenure=data["loan"]["tenure"],
            id_document=id_path,
            income_proof=income_path,
            bank_statement=bank_path
        )

        db.add(loan)
        db.commit()
        db.refresh(loan)

        return loan

    except Exception as e:
        db.rollback()
        raise Exception(f"Loan creation failed: {str(e)}")