import os
from dotenv import load_dotenv

load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
PORT = int(os.getenv("PORT", 8000))

print("[CONFIG] Loaded Twilio Config:")
print("TWILIO_ACCOUNT_SID:", TWILIO_ACCOUNT_SID)
print("TWILIO_PHONE_NUMBER:", TWILIO_PHONE_NUMBER)
print("PORT:", PORT)
