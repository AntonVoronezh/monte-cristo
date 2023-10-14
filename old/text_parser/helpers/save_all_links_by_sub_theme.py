from bs4 import BeautifulSoup
import requests
import fake_useragent
import json

from old.text_parser.settings import domen, theme, sub_theme
from old.text_parser.helpers.set_folders import folders_names


def get_all_links_by_sub_theme():
    url = f'https://www.{domen}/news/{theme}/{sub_theme}'
    ua = fake_useragent.UserAgent()
    fake_ua = {'user-agent': ua.random}
    response = requests.get(url=url, headers=fake_ua)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')

    print(url)
    arr = []
    link_latest = soup.find_all('ul', class_='fa-ul list-padded')

    for txt in link_latest:
        link = txt.find("a").get("href")
        arr.append(f"https://www.{domen}{link}")

    return arr


def save_all_links_by_sub_theme():
    arr = get_all_links_by_sub_theme()
    json_result = {}

    i = 1
    for txt in arr:
        name = txt.split('/')[-1].split('.')[0]
        json_result[i] = {'link': txt, 'name': name}
        i = i + 1

    print(f"Всего ссылок - {i}")
    path = folders_names['links']

    with open(f'{path}/{sub_theme}.json', 'w') as outfile:
        json.dump(json_result, outfile, indent=4)
