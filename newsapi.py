    import requests
    import pandas as pd
    from textblob import TextBlob
    from datetime import datetime
    from textblob import TextBlob

    # Função para buscar notícias
    def fetch_news(api_key, query, from_date, to_date, page_size=100):
        url = f'https://newsapi.org/v2/everything?q={query}&from={from_date}&to={to_date}&pageSize={page_size}&apiKey={api_key}'
        response = requests.get(url)
        
        # Verificar código de status da resposta HTTP
        if response.status_code != 200:
            raise Exception(f"Erro na solicitação: {response.status_code} - {response.text}")
        
        data = response.json()
        
        # Imprimir a resposta completa para depuração
        print("Resposta da API:", data)
        
        # Verificar se a chave 'articles' está presente
        if 'articles' in data:
            return data['articles']
        else:
            # Levantar um erro com uma mensagem mais clara
            raise KeyError("'articles' key not found in the response. Check your API request and credentials.")


    # Função para analisar o sentimento
    def analyze_sentiment(text):
        analysis = TextBlob(text)
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'


    def analyze_sentiment(text):
        analysis = TextBlob(text)
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'
        
    articles_types = ['Business','Entertainment','General','Health','Science','Sports','Technology']

    # Parâmetros de entrada
    api_key = '1bbf3f796a5e495c9ef2fb9f303dff01'
    from_date = '2024-07-01'
    to_date = '2024-07-03'

    # Busca de notícias
    final_df = pd.DataFrame()
    for query in articles_types:
        try:
            articles = fetch_news(api_key, query, from_date, to_date)
            # Criação de DataFrame
            news_df = pd.DataFrame(articles)
            news_df['sentiment'] = news_df['description'].apply(analyze_sentiment)
            news_df['type'] = query
            ###news_df['sentiment'] = news_df['Description'].apply(analyze_sentiment)
            news_df = news_df[['source', 'author', 'title', 'description', 'url', 'publishedAt' , 'sentiment','type']]
            news_df.columns = ['Source', 'Author', 'Title', 'Description', 'URL', 'Published At', 'Sentiment','Type']
            news_df.to_csv('news_sentiment_analysis.csv', index=False)
            print("Dataset criado e salvo com sucesso.")
            pd.concat([final_df, news_df], ignore_index=True)
        except KeyError as e:
            print(f"Erro ao buscar notícias: {e}")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
