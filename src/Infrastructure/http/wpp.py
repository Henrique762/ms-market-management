import random
from twilio.rest import Client
from dotenv import load_dotenv
import os

#### Carregar Variáveis
load_dotenv()

def gerar_codigo():
    codigo = ""
    for num in range(4):
        numero = str(random.randint(1, 9))
        codigo += numero
    return codigo


def gerar_msg(codigo, numero):
    account_sid = os.getenv("TWILIO_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_='whatsapp:+14155238886',
    body=f"Seu Código é:{codigo}",
    to=f"whatsapp:{numero}"
    )
    print(message)

def enviar_msg(numero):
    codigo = gerar_codigo()
    
    gerar_msg(codigo, numero)

enviar_msg('+5511962968213')