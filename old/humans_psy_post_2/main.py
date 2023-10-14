import PIL
import httplib2
from PIL import Image, ImageEnhance, ImageDraw, ImageFont
import os, shutil
from random import choice
import requests
import json

tg_url = 'https://t.me/nfxjdnfxlhxfithjpij'
api_token = '6659447899:AAEe8JjANEGzeZ2TKsRkteM8Bx-TI2vhLlA'
api_chat_id = '-1001802264924'

# tg_url = 'https://t.me/doctor_psyh'
# api_token = '6324718682:AAGPn4xYfKuVo33W1V2Jl93YWnUSUpev_Sk'
# api_chat_id = '-1001698544953'

api_url = f"https://api.telegram.org/bot{api_token}"

realpath = os.path.dirname(os.path.realpath(__file__))

out_folder_path = os.path.join(realpath, 'out')


def remove_folder(item):
    item['text'].close()
    path = item['path']


def get_folder(folder_path):
    folder_list = os.listdir(folder_path)
    r = choice(folder_list)
    text = open(f'{folder_path}/{r}', 'rb')

    return {'text': text, 'path': r}


def parsed_response(url_message, files={}):
    try:
        response = requests.post(url_message, files=files)
        return json.loads(response.text)
    except Exception as e:
        print(e)


def send_message(api_url, chat_id, message):
    url_message = f"{api_url}/sendMessage?chat_id={chat_id}&text={message}&parse_mode=html"
    return parsed_response(url_message)


def post():
    random_folder = get_folder(out_folder_path)

    response = {}
    data = json.load(random_folder['text'])
    # 👁️‍🗨️💬
    # description = data['description']
    description_arr = data['description'].split('.')
    description_arr_filter = list(filter(None, description_arr))
    description_arr_filter_reverse = description_arr_filter[::-1]
    description_without_last = description_arr_filter[:-1]
    last = description_arr_filter_reverse[0]
    description = f'{". ".join(description_without_last)}. \n\n     {last}.'

    sign = f'<a href="{tg_url}">👉 Доктор Фрейд. Подписаться</a>'
    message = f'💬 {description} 😀 \n\n {sign}'

    response = send_message(api_url=api_url, chat_id=api_chat_id, message=message)
    # remove_folder(random_folder)
    print(response)
    print(f'{response["ok"]}, message_id - {response["result"]["message_id"]}')

# post()
