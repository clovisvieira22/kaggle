import requests
from flask import Flask, request, redirect
import webbrowser
import pandas as pd

# Configurações da API
client_id = 'ZVUPM4VLXXDRAC7CR4'
client_secret = 'ZCXH4KZEOJ4PKJIRU3PR7JXPJMUCTDC77QHOUEY4M2N752R3LT'
redirect_uri = 'https://4099-179-35-14-198.ngrok-free.app'  # Atualize com a URL fornecida pelo ngrok
authorization_base_url = 'https://www.eventbrite.com/oauth/authorize'
token_url = 'https://www.eventbrite.com/oauth/token'

# Passo 1: Redirecionar o usuário para a página de autorização
authorization_base_url = 'https://www.eventbrite.com/oauth/authorize'
auth_url = f"{authorization_base_url}?response_type=code&client_id={client_id}&redirect_uri={redirect_uri}"
print(f"Visite esta URL no navegador para autorizar a aplicação: {auth_url}")

# Após autorizar, o navegador será redirecionado para o redirect_uri com um código de autorização.
# Copie o código de autorização da URL e cole no código abaixo.

# Passo 2: Trocar o código de autorização por um token de acesso
authorization_code = input("DVJ6LRGT6Y7IDRXNHNWN")

token_url = 'https://www.eventbrite.com/oauth/token'
token_data = {
    'grant_type': 'authorization_code', 
    'client_id': client_id,
    'client_secret': client_secret,
    'code': authorization_code,
    'redirect_uri': redirect_uri
}
response = requests.post(token_url, data=token_data)
response.raise_for_status()
token_info = response.json()
access_token = token_info['access_token']
print(f"Access token received: {access_token}")

# Agora você tem o token de acesso e pode usá-lo para fazer solicitações à API.
