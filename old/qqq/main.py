import os
from colorama import Fore
from random import choice
from old.qqq.helpers.send_message_func import send_photo_from_file
from old.qqq.helpers.messages_type import get_next_message_type

realpath = os.path.dirname(os.path.realpath(__file__))

img_folder_path = os.path.join(realpath, 'img')
text_folder_path = os.path.join(realpath, 'text')
audio_folder_path = os.path.join(realpath, 'audio')
document_folder_path = os.path.join(realpath, 'document')
poll_folder_path = os.path.join(realpath, 'poll')
quiz_folder_path = os.path.join(realpath, 'quiz')


def remove_file(item):
    item['file'].close()
    os.remove(item['path'])


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


api_token = '6659447899:AAEe8JjANEGzeZ2TKsRkteM8Bx-TI2vhLlA'
api_chat_id = '-1001802264924'
chanal_link = 'nfxjdnfxlhxfithjpij'
chanal_name = 'a1b1c1'

api_url = f"https://api.telegram.org/bot{api_token}"

# script_dir = os.path.dirname(os.path.realpath(__file__))
# path = os.path.join(script_dir)

next_messages_type = get_next_message_type()

if next_messages_type is None:
    print(Fore.RED + "ЗАКОНЧИЛИСЬ ДАННЫЕ")
    exit()

response = {}

# if next_messages_type == 'text_for_msg':
#     random_text_file = get_item(text_folder_path)
#     title = json.load(random_text_file['file'])['title']
#     random_em = choice([
#         '\U0001F449',
#         '\U000027A1',
#         '\U00002714',
#         '\U0001F6A9',
#         '\U0001F4CC'
#     ])
#     random_podval = choice([
#         'Подписаться на канал',
#         'Подписаться',
#         f'Подписаться на {chanal_name}',
#         f'{random_em} @{chanal_name}'
#          ])
#     title_plus = f'{title} \n\n<a href="https://t.me/{chanal_link}">{random_podval}</a>'
#     response = send_big_message(message=title_plus, api_url=api_url, chat_id=api_chat_id)
#     remove_file(random_text_file)
f = '''
  • Mailion - защищенная корпоративная почтовая система на российском рынке с сертификатом ФСТЭК России
 • Продукт предназначен для крупных коммерческих и государственных организаций
 • Включает в себя семь крупных модулей, более 400 собственных компонентов и почти 400 тыс. строк кода
 • Разрабатывался с использованием Polymer, затем переключились на React и Nx
 • Выбор React обусловлен унификацией стека технологий, большой поддержкой сообщества и интеграцией с Nx
 • Nx помогает разделить код на проекты, обеспечить независимую сборку и визуализировать граф зависимостей
 • В будущем планируется подробнее раскрыть роль монорепозитория Nx и веб-компонентов в разработке 
'''
# if next_messages_type == 'img':
#     random_img_file = get_item(img_folder_path)
#     response = send_photo_from_file(api_url=api_url, chat_id=api_chat_id, file_opened=random_img_file['file'], caption='gfhf 77777')
response = send_photo_from_file(api_url=api_url, chat_id=api_chat_id, file_opened=open('back_33.png', 'rb'), caption=f)
#     remove_file(random_img_file)
#
# if next_messages_type == 'audio':
#     random_audio_file = get_item(audio_folder_path)
#     response = send_audio_from_file(api_url=api_url, chat_id=api_chat_id, file_opened=random_audio_file['file'], caption='ffff ggg jjj kkk')
#     remove_file(random_audio_file)
#
# if next_messages_type == 'document':
#     random_document_file = get_item(document_folder_path)
#     response = send_document_from_file(api_url=api_url, chat_id=api_chat_id, file_opened=random_document_file['file'], caption='ffff ggg jjj kkk')
#     remove_file(random_document_file)
#
#
# if next_messages_type == 'poll':
#     random_poll_file = get_item(poll_folder_path)
#     response = send_poll(api_url=api_url, chat_id=api_chat_id, poll=random_poll_file['file'])
#     remove_file(random_poll_file)
#
#
# if next_messages_type == 'quiz':
#     random_quiz_file = get_item(quiz_folder_path)
#     response = send_quiz(api_url=api_url, chat_id=api_chat_id, poll=random_quiz_file['file'])
#     remove_file(random_quiz_file)


# if messages_types[next_messages_type] == 'photo_group_from_file':
#     file_opened_arr =[os.path.join(script_dir, 'img', '1111.jpg'), os.path.join(script_dir, 'img', '222.jpg')]
#     response = send_photo_group_from_file(api_url=api_url, chat_id=api_chat_id, file_opened_arr=file_opened_arr)
#
# save_result(response, api_chat_id, messages_types[next_messages_type])
#
# print(response)
print(f'{response["ok"]}, message_id - {response["result"]["message_id"]}')

# REPOST
# send_repost_message(api_url, api_chat_id, '-1001802264924', 325)
# title = 'fgdg rgetrg rtert rtert \n\n https://t.me/nfxjdnfxlhxfithjpij'
# # title = 'fgdg rgetrg rtert rtert \n\n https://t.me/belarusian_silovik'
# send_big_message(message=title, api_url=api_url, chat_id=api_chat_id)


#
# hh = 'Причин, по которым у человека могут быть заблокированы денежные потоки, немало. Но все они можно разделить на три группы. Установки общества отвергают и тех, и других. Кармические узлы. Когда мы пытаемся стать богаче своих близких это тоже очень сложно, и очень часто встречает препятствие и непонимание среди близких. В сфере влияния ( её ещё называют " чёрной магией " ) есть неограниченные возможности забрать у человека его финансовое благополучие.'
# jj = '''
#  Недосыпание может негативно влиять на когнитивные способности и работоспособность.
#  Лишение сна снижает способность сохранять внимание и приводит к провалам во внимании.
#  Недосыпание приводит к большему количеству ошибок при размещении.
#  Кофеин может улучшить способность обращать внимание, но не уменьшить ошибки при размещении.
#  Дневной сон не оказывает заметного влияния на когнитивные способности после ночи недосыпания.
#  Кофеин и дневной сон не могут заменить полноценный сон для улучшения работоспособности.
#  Достаточный сон необходим для разума и мозговой деятельности.'''
# response = send_big_message(message=jj, api_url=api_url, chat_id=api_chat_id)
