from twilio.rest import Client

from congig import settings

from .models import Contact


def send_whatsapp_notification(message):
    account_sid = settings.TWILIO_ACCOUNT_SID
    auth_token = settings.TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)
    contact = Contact.objects.first()

    from_whatsapp_number = f'whatsapp:{settings.TWILIO_PHONE_NUMBER}'
    to_whatsapp_number = f'whatsapp:{contact.phone_number}'

    message = client.messages.create(
        body=message,
        from_=from_whatsapp_number,
        to=to_whatsapp_number
    )
