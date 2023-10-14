import requests
import json


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
