import importlib
import os
import json
import shutil
from datetime import datetime
from random import choice

import PIL
from PIL import Image, ImageEnhance, ImageDraw, ImageFont
from colorama import Fore


def import_module_from_path(path):
    spec = importlib.util.spec_from_file_location("my_module", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def get_random_elem_name_from_folder(folder_path):
    folder_list = os.listdir(folder_path)
    if len(folder_list) == 0:
        return None

    return choice(folder_list)


def get_file_from_folder_by_name(folder_path, file_name):
    return open(f'{folder_path}/{file_name}', 'rb')


def get_json_field(json_data, field_name):
    if json_data:
        try:
            val = str(json.load(json_data)[field_name])
            return val
        except json.JSONDecodeError as e:
            print(f"Ошибка: {e}")
    else:
        print("JSON строка пуста")

def set_space_before_last_sentence(text):
    description_arr = text.split('.')
    description_arr_out = f'<b>{description_arr[0]}.</b> \n\n'

    for i, el in enumerate(description_arr):
        if i != 0:
             if len(el) > 0:
                description_arr_out = f'{description_arr_out} {el}.'

    return description_arr_out

def remove_file_from_folder(folder_path, file_name):
    path = os.path.join(folder_path, file_name)

    try:
        os.remove(path)
    except OSError as e:
        print(e)


def remove_folder(folder_path):
    try:
        shutil.rmtree(folder_path)
    except OSError as e:
        print(e)


def make_caption(data):
    arr = data.split('.')
    arr2 = []

    for el in arr:
        if len(el) > 0:
            arr2.append(f'{el}. ')
    r = ['🌶']
    return f'{choice(r)} <b>Новость:</b> ' + ''.join(arr2)


def make_morality(data):
    r = ['⚡️']
    return f'{choice(r)} <b>Комментарий:</b> <i>{data}</i>'


def make_image(img_path):
    img_path_back = os.path.join(img_path, 'back.jpg')
    img_path_back_2 = os.path.join(img_path, 'back_2.jpg')
    img_path_back_3 = os.path.join(img_path, 'back_3.jpg')

    im = Image.open(img_path_back)
    # im_crop = im.crop((0, 50, 750, 400))
    fixed_width = 400
    width_percent = (fixed_width / float(im.size[0]))
    height_size = int((float(im.size[1]) * float(width_percent)))
    im = im.resize((fixed_width, height_size))

    # fixed_height = 200
    # width_percent = (fixed_height / float(im.size[1]))
    # width_size = int((float(im.size[0]) * float(width_percent)))
    #     im = im.resize((width_size, fixed_height))
    im .save(img_path_back_2, quality=95)

    im_contrast = Image.open(img_path_back_2)
    enhancer = ImageEnhance.Contrast(im_contrast)
    factor = 1.35
    im_contrast_output = enhancer.enhance(factor)
    enhancer_2 = ImageEnhance.Sharpness(im_contrast_output)
    factor_2 = 1.35
    im_contrast_output_2 = enhancer_2.enhance(factor_2)

    im_contrast_output_2.save(img_path_back_3)

    image = open(img_path_back_3, 'rb')
    return image


def check_folders(name):
    if len(name.split('.')) == 2 or name == 'main.py' or name == 'last_message_type.txt':
        return False
    return True


def check_folders_main(name):
    if len(name.split(
            '.')) == 2 or name == 'main.py' or name == 'old' or name == '.idea' or name == 'b0_in_tg' or name == 'b1_helpers' or name == 'b2_variant_message' or name == 'a0_proba':
        return False
    return True


def get_folders_s_variants(folder_path):
    return list(filter(check_folders, os.listdir(folder_path)))


def write_current_message_type(folder_path, next_messages_type):
    file = open(os.path.join(folder_path, 'last_message_type.txt'), 'w')
    file.write(next_messages_type)
    file.close()


def get_current_message_type(folder_path):
    last_message_type_file = os.path.join(folder_path, 'last_message_type.txt')
    check_file = os.path.isfile(last_message_type_file)

    if check_file is False:
        write_current_message_type(folder_path=folder_path, next_messages_type='None')

    file = open(last_message_type_file, 'r')
    current = file.read()
    return current


def set_new_message_type(folder_path):
    messages_variants = get_folders_s_variants(folder_path=folder_path)
    last_message_type_file = os.path.join(folder_path, 'last_message_type.txt')

    messages_types = []
    for name in messages_variants:
        try:
            d = os.listdir(os.path.join(folder_path, name, 'variants'))

            if 0 < len(d) - 1 < 5:
                print(f'📁 {name}' + Fore.LIGHTYELLOW_EX + f' мало данных ({len(d) - 1})' + Fore.RESET)

            if len(d) == 0:
                print(f'📁 {name}' + Fore.RED + ' закончились данные' + Fore.RESET)

            if len(d) != 0:
                messages_types.append(name)
        except:
            pass

    if len(messages_types) == 0:
        print('❗❗❗❗❗❗❗❗❗❗❗❗❗❗  ВСЁ ЗАКОНЧИЛОСЬ  ❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗❗')
        return None

    try:
        file = open(last_message_type_file, 'r')
    except:
        write_current_message_type(folder_path=folder_path, next_messages_type='None')
        file = open(last_message_type_file, 'r')

    last_messages_type = file.read()

    if last_messages_type == 'None' or len(last_messages_type) == 0 or last_messages_type not in messages_types:
        next_messages_type = choice(messages_types)
    else:
        last_messages_type_index = messages_types.index(last_messages_type)

        next_messages_type_index = last_messages_type_index + 1 if last_messages_type_index + 1 <= len(
            messages_types) - 1 else 0
        next_messages_type = messages_types[next_messages_type_index]

    ff = open(last_message_type_file, 'w')
    ff.write(next_messages_type)
    ff.close()

    return next_messages_type


def write_message_response(message_type, folder_path, response):
    current_time = datetime.now().time()
    current_time_split = str(current_time).split('.')
    response_id = response['result']['message_id']

    if message_type == 'message_text_bez_title_i_img':
        response_text = response['result']['text'][:50]
    if message_type == 'message_img_s_title_i_text':
        response_text = response['result']['caption'][:50]

    row = f'{current_time_split[0]}|{message_type}|{response_id}|{response_text}\n'

    file = open(os.path.join(folder_path, 'messages-log.txt'), 'a', encoding="utf-8")
    file.write(row)
    file.close()
