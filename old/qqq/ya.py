import requests
from bs4 import BeautifulSoup
import fake_useragent
from colorama import Fore

ua = fake_useragent.UserAgent()
fake_ua = {'user-agent': ua.random}

endpoint = 'https://300.ya.ru/api/sharing-url'
token = 'y0_AgAAAAAspYMlAAoX4wAAAADs1dppUcdSkX1YSGycCzrrIdDNv019cS0'

response = requests.post(
    endpoint,
    json={
        'article_url': 'https://www.simplypsychology.org/wernickes-area.html'
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
print(pre_title["content"].replace('Краткий пересказ:', '') if pre_title else "No meta title given")
print(pre_description["content"] if pre_description else "No meta title given")