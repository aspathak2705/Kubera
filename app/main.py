from fastapi import FastAPI
from app.config import settings
from app.db import engine, Base
from app.models import applicant, loan_application
from app.routes.loan_routes import router as loan_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG
)

app.include_router(loan_router)

@app.get("/")
def root():
    return {
        "message": f"Welcome to {settings.APP_NAME}"
    }

@app.get("/health")
def health_check():
    return {
        "status": "OK"
    }

