import requests
from flask import Flask, request, redirect
import webbrowser
import pandas as pd
import os

# Configurações da API
client_id = 'ZVUPM4VLXXDRAC7CR4'
client_secret = 'ZCXH4KZEOJ4PKJIRU3PR7JXPJMUCTDC77QHOUEY4M2N752R3LT'
redirect_uri = 'https://aa3b-179-35-14-198.ngrok-free.app'  # Atualize com a URL fornecida pelo ngrok
authorization_base_url = 'https://www.eventbrite.com/oauth/authorize'
token_url = 'https://www.eventbrite.com/oauth/token'

# Inicialize o app Flask
app = Flask(__name__)

@app.route('/')
def index():
    # Redireciona o usuário para a página de autorização do Eventbrite
    auth_url = f"{authorization_base_url}?response_type=code&client_id={client_id}&redirect_uri={redirect_uri}"
    print(f"Redirecting to: {auth_url}")  # Adicione esta linha para depurar
    return redirect(auth_url)

@app.route('/callback')
def callback():
    # Recebe o código de autorização
    authorization_code = request.args.get('code')
    print(f"Authorization code received: {authorization_code}")  # Adicione esta linha para depurar
    if not authorization_code:
        return "Error: Authorization code not found"

    # Troca o código de autorização por um token de acesso
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
    print(f"Access token received: {access_token}")  # Adicione esta linha para depurar

    # Use o token de acesso para obter informações sobre as categorias
    headers = {
        'Authorization': f'Bearer {access_token}',
    }
    categories_url = 'https://www.eventbriteapi.com/v3/categories/'
    response = requests.get(categories_url, headers=headers)
    response.raise_for_status()
    categories_data = response.json()
    print(f"Categories data: {categories_data}")  # Adicione esta linha para depurar

    # Transforme os dados das categorias em um DataFrame do pandas
    categories_list = []
    for category in categories_data['categories']:
        category_info = {
            'ID': category['id'],
            'Name': category['name']
        }
        categories_list.append(category_info)
    categories_df = pd.DataFrame(categories_list)

    # Exibir o DataFrame
    print(categories_df)

    # Opcionalmente, você pode salvar o DataFrame em um arquivo CSV
    categories_df.to_csv('categories.csv', index=False)

    return 'Autenticação realizada com sucesso! Verifique o console para os dados das categorias.'

# Inicie o navegador e o servidor Flask
if __name__ == '__main__':
    port = 8080  # Altere para a porta desejada, se necessário
    webbrowser.open(f'http://localhost:{port}')
    app.run(debug=True, port=port)