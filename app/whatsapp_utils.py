import os
import requests
from dotenv import load_dotenv
load_dotenv()

def enviar_mensaje(numero, texto):
    url = f"https://graph.facebook.com/v19.0/{os.getenv('WHATSAPP_PHONE_ID')}/messages"
    headers = {
        "Authorization": f"Bearer {os.getenv('WHATSAPP_TOKEN')}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": numero,
        "type": "text",
        "text": {"body": texto}
    }
    response = requests.post(url, headers=headers, json=payload)
    print("Mensaje enviado:", response.status_code, response.text)
