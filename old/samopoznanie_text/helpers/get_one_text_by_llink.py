from bs4 import BeautifulSoup
import requests
import fake_useragent
import json
from old.samopoznanie_text.helpers.sber import get_sber_summary


def get_text_by_link(link):
    ua = fake_useragent.UserAgent()
    fake_ua = {'user-agent': ua.random}
    response = requests.get(url=link, headers=fake_ua)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')

    article_name = soup.find('h1')
    article_text_paragraph = soup.find('div', class_='object_description for-avatar-block')

    text = []

    for paragraph in article_text_paragraph:
        paragraph_text = paragraph.text.replace(' ', ' ').replace('\n', '')
        if len(paragraph_text) != 0:
            text.append(paragraph_text)
    # print(link)
    # summary_ya = get_ya_summary(link)
    summary_sber = get_sber_summary(" ".join(text))

    json_result = {
        'title': article_name.text.replace(' ', ' '),
        'summary_sber':  summary_sber,
        # 'summary_ya':  summary_ya,
        'text_for_msg': text,
    }

    name = link.split('/')[-2]
    with open(f"text_for_msg/{name}.json", 'w', encoding='utf-8') as outfile:
        json.dump(json_result, outfile, indent=4, ensure_ascii=False)

    print(f'{name} - {len(summary_sber)}')
