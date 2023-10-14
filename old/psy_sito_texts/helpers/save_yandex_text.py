import time
import json


def save_yandex_text(text):
    description_arr = []
    arr = text['description'].split('•')

    for elem in arr:
        strip_elem = elem.strip()
        if len(strip_elem) > 0:
            description_arr.append(strip_elem)

    json_result = {'title': text['title'], 'description': description_arr}

    with open(f'text_for_msg/{time.time()}.json', 'w', encoding='utf-8') as outfile:
        json.dump(json_result, outfile, indent=4, ensure_ascii=False)

