from bs4 import BeautifulSoup
import requests
import fake_useragent
import json

link = 'https://samopoznanie.ru/objects.php?action=get_object_list'


def get_all_links(start):
    ua = fake_useragent.UserAgent()
    fake_ua = {'user-agent': ua.random}

    data = {
        'filter': 0,
        'start': 2,
        'object_type': 8,
        'moderated': 1,
        'atribs''': ['message_count', 'owner_id', 'created', 'moderated', 'rubrics', 'rating', 'rating', 'linked_objects','has_video', 'options','description',  'author' ],
        'url': 'https://samopoznanie.ru/articles/?rubric=0410'
    }

    # session = requests.Session()
    # session.get(url='https://samopoznanie.ru/articles/?rubric=040810', headers=fake_ua)
    # response = session.post(url=link, data=json.dumps(data))
    # # response = session.get(url='https://samopoznanie.ru/articles/?rubric=040810', headers=fake_ua)
    # print(response.cookies)
    # # response = requests.post(url=link, headers=fake_ua, data=json.dumps(data), cookies=cookies)
    # response.encoding = 'utf-8'
    # soup = BeautifulSoup(response.text_for_msg, 'lxml')
    # print(soup)

    URL1 = 'https://samopoznanie.ru/articles/?rubric=0410'
    URL2 = 'https://samopoznanie.ru/objects.php?action=get_object_list'

    session = requests.Session()
    headers = {
        'accept': 'text_for_msg/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'uk,en-US;q=0.9,en;q=0.8,ru;q=0.7',
        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
    }
    r = session.get(url=URL1, headers=headers)
    r2 = session.post(url=URL2, data=json.dumps(data))
    print(list(session))
    print(r2)


get_all_links(2)
