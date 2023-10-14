import requests
import json

api_token = '6659447899:AAEe8JjANEGzeZ2TKsRkteM8Bx-TI2vhLlA'
api_chat_id = '-1001802264924'
api_url = f"https://api.telegram.org/bot{api_token}"

def parsed_response(url_message, files={}):
    try:
        response = requests.post(url_message, files=files)
        print(response)
        return json.loads(response.text)
    except Exception as e:
        print(e)


def send_message(api_url, chat_id, message_id):


    url_message = f"{api_url}/setDefaultReaction?chat_id={chat_id}&message_id={message_id}"
    return parsed_response(url_message)


send_message(api_url, api_chat_id, '738')