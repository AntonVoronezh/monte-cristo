import requests
import json


def send_message(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"

    try:
        response = requests.post(url, json={'chat_id': chat_id, 'text_for_msg': message})
        parsed_response = json.loads(response.text)
        # print(json.dumps(parsed_response, indent=8))
    except Exception as e:
        print(e)
