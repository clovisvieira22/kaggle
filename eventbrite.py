import requests
from flask import Flask, request, redirect
import webbrowser
import pandas as pd

# Configurações da API
client_id = '7VZ7DIYIIDGWB7ATI'
client_secret = 'CPM3XCE2HSMU7SV5IYEY3RTL2GFHU22LDDMMEI2UE4SGJF6CMM'
redirect_uri = 'https://aa3b-179-35-14-198.ngrok-free.app'  # Certifique-se de que este URI é o mesmo configurado no Eventbrite
authorization_base_url = 'https://www.eventbrite.com/oauth/authorize'
token_url = 'https://www.eventbrite.com/oauth/token'

# Inicialize o app Flask
app = Flask(__name__)

@app.route('/')
def index():
    try:
        # Redireciona o usuário para a página de autorização do Eventbrite
        auth_url = f"{authorization_base_url}?response_type=code&client_id={client_id}&redirect_uri={redirect_uri}"
        return redirect(auth_url)
    except Exception as e:
        return f"Error in index: {e}"

@app.route('/callback')
def callback():
    try:
        # Recebe o código de autorização
        authorization_code = request.args.get('code')
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
        response.raise_for_status()  # Raise an error for bad HTTP status codes
        token_info = response.json()
        
        if 'access_token' not in token_info:
            return f"Error: access_token not found in response: {token_info}"
        
        access_token = token_info['access_token']
        
        # Use o token de acesso para obter informações sobre eventos
        headers = {
            'Authorization': f'Bearer {access_token}',
        }
        events_url = 'https://www.eventbriteapi.com/v3/categories/'
        response = requests.get(events_url, headers=headers)
        response.raise_for_status()  # Raise an error for bad HTTP status codes
        events_data = response.json()
        
        if 'events' not in events_data:
            return f"Error: events not found in response: {events_data}"
        
        events = events_data['events']
        
        # Transforme os dados dos eventos em um DataFrame do pandas
        events_list = []
        for event in events:
            event_info = {
                'ID do Evento': event['id'],
                'Nome': event['name']['text'],
                'Início': event['start']['local'],
                'Fim': event['end']['local']
            }
            events_list.append(event_info)
        events_df = pd.DataFrame(events_list)
        
        # Exibir o DataFrame
        print(events_df)
        
        # Opcionalmente, você pode salvar o DataFrame em um arquivo CSV
        events_df.to_csv('eventos.csv', index=False)

        return 'Autenticação realizada com sucesso! Verifique o console para os dados dos eventos.'
    except requests.exceptions.RequestException as e:
        return f"Error in callback: {e}"
    except Exception as e:
        return f"Error in callback: {e}"

# Inicie o navegador e o servidor Flask
if __name__ == '__main__':
    webbrowser.open('http://localhost:5000')
    app.run(port=5000, debug=True)


