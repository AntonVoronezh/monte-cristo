import os
from random import choice
from colorama import Fore

from b0_in_tg.main import send_photo_from_file
from b1_helpers.main import get_random_elem_name_from_folder, get_file_from_folder_by_name, get_json_field, \
    make_caption, make_morality, remove_folder, make_image, write_message_response


def message_img_s_title_i_text(api_url, api_chat_id, real_path, folder_name, sign, is_remove):
    message_type = 'картинка с титлом и текстом'
    message_folder_name = 'message_img_s_title_i_text'
    folder_path = os.path.join(real_path, folder_name)
    message_folder_path = os.path.join(folder_path, message_folder_name)
    variants_folder_path = os.path.join(message_folder_path, 'variants')
    random_elem_name = get_random_elem_name_from_folder(folder_path=variants_folder_path)
    variants_folder_path_img = os.path.join(variants_folder_path, random_elem_name)

    if random_elem_name is None:
        print(Fore.LIGHTRED_EX + f'"{folder_name}" закончились данные' + Fore.BLUE + f' ({message_type})')
        return None
    else:
        random_folder_path = os.path.join(real_path, folder_name, message_folder_name, 'variants', random_elem_name)
        random_elem_file_json_title = get_file_from_folder_by_name(folder_path=random_folder_path,
                                                                   file_name='text.json')
        random_elem_file_json_description = get_file_from_folder_by_name(folder_path=random_folder_path,
                                                                         file_name='text.json')
        random_elem_file_morality = get_file_from_folder_by_name(folder_path=random_folder_path, file_name='text.json')

        title_from_file = get_json_field(json_data=random_elem_file_json_title, field_name='title')
        description_from_file = get_json_field(json_data=random_elem_file_json_description, field_name='description')
        morality_from_file = get_json_field(json_data=random_elem_file_morality, field_name='morality')

        description = make_caption(data=description_from_file)
        morality = make_morality(data=morality_from_file)

        caption = f'<b>{title_from_file}</b> \n\n {description} \n\n {morality} \n\n {sign}'

        random_elem_file_json_title.close()
        random_elem_file_json_description.close()
        random_elem_file_morality.close()

        image = make_image(variants_folder_path_img)

        if caption and image:
            response = send_photo_from_file(api_url=api_url, chat_id=api_chat_id, image=image,
                                            caption=caption)
            image.close()

            if response["ok"]:
                print(f'✔️ {message_type}')
                print(Fore.WHITE + f'{response["ok"]}, message_id - {response["result"]["message_id"]}' + Fore.RESET)
                write_message_response(message_type=message_folder_name, folder_path=folder_path, response=response)

                if is_remove:
                    remove_folder(folder_path=variants_folder_path_img)

                return response
            else:
                print(f'⛔ {message_type}')
                return {}
