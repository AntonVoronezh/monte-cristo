import PIL
import httplib2
from PIL import Image, ImageEnhance, ImageDraw, ImageFont
import os,  shutil
from random import choice
import requests
import json

# tg_url = 'https://t.me/aaaaaaa'
# api_token = '6659447899:AAEe8JjANEGzeZ2TKsRkteM8Bx-TI2vhLlA'
# api_chat_id = '-1001802264924'

tg_url = 'https://t.me/doctor_psyh'
api_token = '6324718682:AAGPn4xYfKuVo33W1V2Jl93YWnUSUpev_Sk'
api_chat_id = '-1001698544953'

api_url = f"https://api.telegram.org/bot{api_token}"



realpath = os.path.dirname(os.path.realpath(__file__))

out_folder_path = os.path.join(realpath, 'out')

def get_image(dir):
    im = Image.open(f'out/{dir}/back.jpg')
    im_crop = im.crop((0, 50, 750, 400))
    im_crop.save('121212-2.jpg', quality=95)

    im_contrast = Image.open('121212-2.jpg')
    im_contrast_rotate =im_contrast.transpose(PIL.Image.FLIP_LEFT_RIGHT)
    enhancer = ImageEnhance.Contrast(im_contrast_rotate)
    factor = 1.35
    im_contrast_output = enhancer.enhance(factor)
    enhancer_2 = ImageEnhance.Sharpness(im_contrast_output)
    factor_2 = 1.35
    im_contrast_output_2 = enhancer_2.enhance(factor_2)

    draw = ImageDraw.Draw(im_contrast_output_2)
    font = ImageFont.truetype("trebuc.ttf", size=30)
    draw.ellipse((530, 300, 570, 340), fill='#ffffff')
    draw.ellipse((695, 300, 735, 340), fill='#ffffff')
    draw.rectangle((550, 300, 710, 340), fill='#ffffff')
    draw.text((540, 300), '@doctor_psyh', '#000000', font)

    im_contrast_output_2.save('121212-3.jpg')



def remove_folder(item):
    item['img'].close()
    item['text'].close()
    path = item['path']
    shutil.rmtree(f'out/{path}')

def get_folder(folder_path):
    folder_list = os.listdir(folder_path)
    r = choice(folder_list)
    get_image(r)
    text = open(f'out/{r}/text.json', 'rb')
    img = open(f'121212-3.jpg', 'rb')
    return {'text': text, 'path': r, 'img': img}


def parsed_response(url_message, files={}):
    try:
        response = requests.post(url_message, files=files)
        return json.loads(response.text)
    except Exception as e:
        print(e)

def send_photo_from_file(api_url, chat_id, file_opened, caption=''):
    url_message = f"{api_url}/sendPhoto?chat_id={chat_id}&caption={caption}&parse_mode=html"
    files = {'photo': file_opened}
    return parsed_response(url_message, files)


def make_caption(data):
    arr = data.split('.')
    arr2 = []
    i = 1
    for el in arr:
        if len(el) > 0:
            arr2.append(f'{el}. ')
            i = i+1
    r = ['📝','🧷','✔️', '✍️', '📰', '📚', '🏷️', '📖' ]

    return f'{choice(r)} ' + ''.join(arr2)
# 💬
def make_morality(data):
    r = ['📌', '⁉️', '‼️️']
    return f'{choice(r)} ️️{data}'

random_folder = get_folder(out_folder_path)



response = {}
data = json.load(random_folder['text'])

title = data['title']
description = make_caption(data['description'])
morality = make_morality(data['morality'])
sign = f'<a href="{tg_url}">👉 Доктор Фрейд. Подписаться</a>'
caption = f'<b>{title}</b> \n\n {description} \n\n {morality} \n\n {sign}'


response = send_photo_from_file(api_url=api_url, chat_id=api_chat_id, file_opened=random_folder['img'],
                                caption=caption)
remove_folder(random_folder)
print(f'{response["ok"]}, message_id - {response["result"]["message_id"]}')
