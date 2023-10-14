from bs4 import BeautifulSoup
import requests
import fake_useragent
import time
import json
import httplib2
import os


def get_image(url, name):
    h = httplib2.Http('.cache')
    response, content = h.request(url)
    out = open(f'out/{name}/back.jpg', 'wb')
    out.write(content)
    out.close()


with open("all_links_i_img.txt") as file:
    lines = [row.strip() for row in file]

plus_text = '''
верни json {
"title": короткий кликбейт заголовок-мнение для текста на русском языке,

"description": главные тезисы текста в художественно-публицистическом жанре с использованием одного образного сравнения длиной 2 предложения по 15 слов на русском языке, 

"morality": веселый, оптимистический  совет на основе вывода из текста на русском языке длиной 1 предложение

},  

текст -
'''
def get_text(link):
    ua = fake_useragent.UserAgent()
    fake_ua = {'user-agent': ua.random}
    response = requests.get(url=link, headers=fake_ua)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')

    article_text = soup.find('div', class_='entry-content body-color clearfix link-color-wrap')
    article_text_paragraphs = article_text.find_all('p')
    arr = []
    i = 0
    for p in article_text_paragraphs:
        if not "Original Research:" in p.text:
            if not "Summary:" in p.text:
                if not "Author:" in p.text:
                    if not "[" in p.text:
                        if len( p.text) > 100:
                            # print(i, p.text)
                            i = i + 1
                            arr.append(p.text)
    # print(arr)
    f = ' '.join(arr)
    return f'{plus_text} {f}'


for i, line in enumerate(lines):
    link_split = line.split("***")
    link = link_split[1]
    img = link_split[0]
    num = str(i)
    text = get_text(link)
    os.makedirs(f'out/{num}')
    file_name = os.path.join(num, 'text')
    print(i, link, flush=True)
    with open(f'out/{num}/text.json', 'w', encoding='utf-8') as outfile:
        json.dump(text, outfile, indent=4, ensure_ascii=False)

    get_image(img, num)
