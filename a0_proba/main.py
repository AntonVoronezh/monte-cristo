import os
from b1_helpers.main import set_new_message_type
from b2_variant_message.message_text_bez_title_i_img.main import message_text_bez_title_i_img
from b2_variant_message.message_img_s_title_i_text.main import message_img_s_title_i_text

project = 'a0_proba'
tg_url = 'https://t.me/nfxjdnfxlhxfithjpij'
api_token = '6659447899:AAEe8JjANEGzeZ2TKsRkteM8Bx-TI2vhLlA'
api_chat_id = '-1001802264924'
api_url = f"https://api.telegram.org/bot{api_token}"
sign = f'<a href="{tg_url}">👉 Я есть Фрейд! Подписаться</a>'
is_remove = False

realpath = os.path.dirname(os.path.realpath(__file__))
realpath_replaced = realpath.replace(project, '')


def start():
    print(f'🔴 {project}')
    next_messages_type = set_new_message_type(folder_path=realpath)

    if next_messages_type == 'message_text_bez_title_i_img':
        message_text_bez_title_i_img(
            api_url=api_url,
            api_chat_id=api_chat_id,
            real_path=realpath_replaced,
            folder_name=project,
            sign=sign,
            is_remove=is_remove,
            emoji={'start': '💬', 'end': '👆'}
        )

    if next_messages_type == 'message_img_s_title_i_text':
        message_img_s_title_i_text(
            api_url=api_url,
            api_chat_id=api_chat_id,
            real_path=realpath_replaced,
            folder_name=project,
            sign=sign,
            is_remove=is_remove,
        )
