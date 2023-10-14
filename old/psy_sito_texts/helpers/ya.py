import requests
from bs4 import BeautifulSoup
import fake_useragent
from colorama import Fore


def get_yandex_text_by_link(article_url):
    ua = fake_useragent.UserAgent()

    endpoint = 'https://300.ya.ru/api/sharing-url'
    token = 'y0_AgAAAAAspYMlAAoX4wAAAADs1dppUcdSkX1YSGycCzrrIdDNv019cS0'

    response = requests.post(
        endpoint,
        json={
            'article_url': article_url
        },
        headers={'Authorization': f'OAuth {token}', 'user-agent': ua.random }
    )

    response_json = response.json()

    if response_json['status'] == 'error':
        print(Fore.RED + "НЕТ ДАННЫХ")
        exit()

    sharing_url = response_json['sharing_url']
    response_sharing_url = requests.get(sharing_url)
    response_sharing_url.encoding = 'utf-8'
    soup = BeautifulSoup(response_sharing_url.text, 'lxml')
    pre = soup.find_all('pre', class_='svelte-1tflzpo')
    # print(soup)
    # svelte-1tflzpo
    # print(pre    )
    # for txt in pre:
    #     print(txt.text_for_msg.replace('•', ''))

    # print(soup)
    pre_title = soup.find('meta',  property="og:title")
    pre_description = soup.find('meta',  property="og:description")

    title = pre_title["content"].replace('Краткий пересказ:', '') if pre_title else None
    description = pre_description["content"] if pre_description else None

    obj = {
        'title':  title,
        'description':  description
    }

    return obj
