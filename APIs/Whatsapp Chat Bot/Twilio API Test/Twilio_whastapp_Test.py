import os
from dotenv import load_dotenv
from twilio.rest import Client

# Loading environmental variables which include clients secrets
load_dotenv()

# CONSTANTS
ACCOUNT_SID = os.getenv('TWILIO_ID')
AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_NUMBER = os.getenv('TWILIO_NUMBER')
client = Client(ACCOUNT_SID, AUTH_TOKEN)


# MESSAGE SENDING DEMO
message = client.messages.create(
  from_=f'whatsapp:{TWILIO_NUMBER}',
  body='Holi, estoy probando la API de Twilio para mandar mensajes de whatsapp...',
  to='whatsapp:+573205503934'
)

print(message.sid)


# the Twilio_response.json contains: 201 - CREATED - The request was successful. We created a new resource and the response body contains the representation.