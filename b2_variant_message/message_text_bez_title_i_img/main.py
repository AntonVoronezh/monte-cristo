import os

from colorama import Fore

from b0_in_tg.main import send_message
from b1_helpers.main import get_random_elem_name_from_folder, get_file_from_folder_by_name, get_json_field, \
    set_space_before_last_sentence, remove_file_from_folder, write_message_response


def message_text_bez_title_i_img(api_url, api_chat_id, real_path, folder_name, sign, is_remove, emoji):
    message_type = 'текст без титла и картинки'
    message_folder_name = 'message_text_bez_title_i_img'
    folder_path = os.path.join(real_path, folder_name)
    message_folder_path = os.path.join(folder_path, message_folder_name)
    variants_folder_path = os.path.join(message_folder_path, 'variants')
    random_elem_name = get_random_elem_name_from_folder(folder_path=variants_folder_path)

    if random_elem_name is None:
        print(Fore.LIGHTRED_EX + f'"{folder_name}" закончились данные' + Fore.BLUE + f' ({message_type})')
        return None
    else:
        random_elem_file_json_text = get_file_from_folder_by_name(folder_path=variants_folder_path, file_name=random_elem_name)
        random_elem_file_json_description = get_file_from_folder_by_name(folder_path=variants_folder_path, file_name=random_elem_name)

        description_from_file = get_json_field(json_data=random_elem_file_json_description, field_name='description')
        text_from_file = get_json_field(json_data=random_elem_file_json_text, field_name='text')
        emoji_start = emoji['start']
        emoji_end = emoji['end']
        text = set_space_before_last_sentence(text=text_from_file)

        message = f'{emoji_start} {text} \n\n {emoji_end} {description_from_file}'

        random_elem_file_json_text.close()
        random_elem_file_json_description.close()

        response = send_message(api_url=api_url, chat_id=api_chat_id, message=message)

        if response["ok"]:
            print(f'✔️ {message_type}')
            print(Fore.WHITE + f'{response["ok"]}, message_id - {response["result"]["message_id"]}' + Fore.RESET)
            write_message_response(message_type=message_folder_name, folder_path=folder_path, response=response)

            if is_remove:
                remove_file_from_folder(folder_path=variants_folder_path, file_name=random_elem_name)
            return response
        else:
            print(f'⛔ {message_type}')
            return {}
