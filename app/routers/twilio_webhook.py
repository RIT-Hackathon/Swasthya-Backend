from fastapi import APIRouter, Request, Form, Response  

router = APIRouter()

@router.post("/whatsapp-webhook")
async def whatsapp_webhook(request: Request):
    form_data = await request.form()  # Extract form data instead of JSON
    data = dict(form_data)  # Convert to dictionary
    print(f"[DEBUG] Received WhatsApp webhook: {data}")

    # Twilio expects XML response
    twiml_response = f"""
    <?xml version="1.0" encoding="UTF-8"?>
    <Response>
        <Message>Thanks for your message!</Message>
    </Response>
    """
    
    return Response(content=twiml_response, media_type="application/xml")
