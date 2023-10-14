import requests
from bs4 import BeautifulSoup

endpoint = 'https://300.ya.ru/api/sharing-url'
token = 'y0_AgAAAABwzw51AAoX4wAAAADswGcDQuNDUIQQQMWGUQOLXE0e58i3e08'


def get_ya_summary(link):
    response = requests.post(
        endpoint,
        json={
            'article_url': link
        },
        headers={'Authorization': f'OAuth {token}'}
    )

    response_json = response.json()
    print(response_json)
    sharing_url = response_json['sharing_url']

    response_sharing_url = requests.get(sharing_url)
    response_sharing_url.encoding = 'utf-8'
    soup = BeautifulSoup(response_sharing_url.text, 'lxml')
    pre = soup.find_all('pre', class_='svelte-1tflzpo')

    arr = []
    for txt in pre:
        arr.append(txt.text.replace('•', ''))

    return arr
