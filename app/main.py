from fastapi import FastAPI
from app.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG
)

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