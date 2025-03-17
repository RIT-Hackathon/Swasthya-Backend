import logging
from fastapi import FastAPI
from app.routers import twilio_webhook
from app.config import PORT

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Include WhatsApp Webhook Router
app.include_router(twilio_webhook.router, prefix="/webhook", tags=["Twilio Webhook"])

@app.get("/")
def root():
    return {"message": "Welcome to the WhatsApp Appointment System!"}

if __name__ == "__main__":
    import uvicorn
    logger.info(f"Starting FastAPI server on port {PORT}")
    uvicorn.run(app, host="0.0.0.0", port=PORT)
