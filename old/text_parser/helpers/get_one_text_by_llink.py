from bs4 import BeautifulSoup
import requests
import fake_useragent
from googletrans import Translator
import json

from old.text_parser.helpers.set_folders import folders_names

def get_text_by_link(url):
    translator = Translator()
    ua = fake_useragent.UserAgent()
    fake_ua = {'user-agent': ua.random}
    response = requests.get(url=url, headers=fake_ua)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    translator = Translator()

    article_name = soup.find('h1', class_='headline')
    article_summary = soup.find('dd', id='abstract')
    article_fullstory_first = soup.find('p', class_='lead', id='first')
    article_fullstory_text = soup.find(id='text_for_msg').find_all('p')

    article_name_ru = translator.translate(article_name.text, dest='ru').text
    article_summary_ru = translator.translate(article_summary.text, dest='ru').text
    article_fullstory_first_ru = translator.translate(article_fullstory_first.text, dest='ru').text

    name = url.split('/')[-1].split('.')[0]
    json_result = {
        # 'en': {
        'title': article_name.text,
        'summary': article_summary.text,
        'first': article_fullstory_first.text,
        'text_for_msg': [],
        # },
        # 'ru': {
        #     'title': article_name_ru,
        #     'summary': article_summary_ru,
        #     'first': article_fullstory_first_ru,
        #     'text_for_msg': [],
        # }
    }

    i = 0
    for txt in article_fullstory_text:
        if txt.find('em'):
            continue
        else:
            # print(txt.text_for_msg)
            json_result['text_for_msg'].append(txt.text)
            # txt_ru = translator.translate(txt.text_for_msg, dest='ru')
            # json_result['ru']['text_for_msg'].append(txt_ru.text_for_msg)
            i = i + 1

    path = folders_names['text_for_msg']
    with open(f"{path}/{name}.json", 'w', encoding='utf-8') as outfile:
        json.dump(json_result, outfile, indent=4, ensure_ascii=False)

