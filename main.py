import requests

url = 'https://newsapi.org/v2/everything?' \
                            'q=ubuntu&' \
                            'from=2022-12-26&' \
                            'sortBy=publishedAt&' \
                            'apiKey=0b31d5b365fb42fb8f2d249f343bf98a'

request = requests.get(url)
content = request.json()

for article in content['articles']:
    print(article['title'])