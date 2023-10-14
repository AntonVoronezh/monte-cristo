import os
from random import choice
from old.psy_sito_send.helpers.send_func import send_photo_from_file
from old.psy_sito_send.helpers.make_caption import make_caption
from old.psy_sito_send.helpers.get_title import get_title
from old.psy_sito_send.helpers.get_title_and_caption import get_title_and_caption
from old.psy_sito_send.helpers.text_on_img import text_on_image

# @psy_sito_bot
# api_token = '6326996969:AAF_zQbKFdmJErohqenwdpLRa1mVYkXZs24'
# api_chat_id = '-1001920988279'
#  a1b1c1 https://t.me/nfxjdnfxlhxfithjpij_bot  @nfxjdnfxlhxfithjpij_bot
api_token = '6659447899:AAEe8JjANEGzeZ2TKsRkteM8Bx-TI2vhLlA'
api_chat_id = '-1001802264924'

api_url = f"https://api.telegram.org/bot{api_token}"

realpath = os.path.dirname(os.path.realpath(__file__))

img_folder_path = os.path.join(realpath, 'img_for_msg')
img_back_folder_path = os.path.join(realpath, 'img_back')
text_folder_path = os.path.join(realpath, 'text_for_msg')


def remove_file(item):
    item['file'].close()
    os.remove(item['path'])

def get_img(folder_path):
    folder_list = os.listdir(folder_path)

    def check_folders(name):
        if name == 'num.txt':
            return False
        return True

    folder_list = list(filter(check_folders, folder_list))

    f = open('img_for_msg/num.txt', 'r')
    last_img_index = f.read()
    f.close()

    next_last_img_index = int(last_img_index) + 1 if int(last_img_index) + 1 <= len(folder_list) - 1 else 0

    with open("img_for_msg/num.txt", "w+") as newFile:
        newFile.write(str(next_last_img_index))
        newFile.close()

    g = folder_list[next_last_img_index]
    item_path = os.path.join(folder_path, g)

    file = open(item_path, 'rb')

    return {'file': file, 'path': item_path}

def get_img_back(folder_path):
    folder_list = os.listdir(folder_path)
    def check_folders(name):
        if name == 'num.txt':
            return False
        return True

    folder_list = list(filter(check_folders, folder_list))

    f = open('img_back/num.txt', 'r')
    last_img_index = f.read()
    f.close()

    next_last_img_index = int(last_img_index) + 1 if int(last_img_index) + 1 <= len(folder_list) - 1 else 0

    with open("img_back/num.txt", "w+") as newFile:
        newFile.write(str(next_last_img_index))
        newFile.close()

    return folder_list[next_last_img_index]


def get_item(folder_path):
    folder_list = os.listdir(folder_path)

    if len(folder_list) == 0:
        split = folder_path.split('\\')[-1]
        print(f'No files in "{split}"')
        return None

    random_item = choice(folder_list)
    item_path = os.path.join(folder_path, random_item)
    file = open(item_path, 'rb')

    return {'file': file, 'path': item_path}


random_text_file = get_item(text_folder_path)
random_img_back_file_name = get_img_back(img_back_folder_path)
print(random_img_back_file_name)
title_and_caption = get_title_and_caption(random_text_file['file'])


title_from_file = get_title(title_and_caption['title'])
caption_from_file = make_caption(title_and_caption['description'])
# print(caption_from_file)
text_on_image(img_back_folder_path, img_folder_path, random_img_back_file_name, title_from_file)
random_img_file = get_img(img_folder_path)




response = {}

response = send_photo_from_file(api_url=api_url, chat_id=api_chat_id, file_opened=random_img_file['file'],
                                caption=caption_from_file)
remove_file(random_text_file)
remove_file(random_img_file)

print(f'{response["ok"]}, message_id - {response["result"]["message_id"]}')
