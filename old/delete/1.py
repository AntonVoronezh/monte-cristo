import requests
import json

tg_url = 'https://t.me/nfxjdnfxlhxfithjpij'
api_token = '6659447899:AAEe8JjANEGzeZ2TKsRkteM8Bx-TI2vhLlA'
api_chat_id = '-1001802264924'
api_url = f"https://api.telegram.org/bot{api_token}"


# 665

def parsed_response(url_message, files={}):
    try:
        response = requests.post(url_message, files=files)
        return json.loads(response.text)
    except Exception as e:
        print(e)


def delete_message(api_url, chat_id, message_id):
    url_chat = f"{api_url}/deleteMessage?chat_id={chat_id}&message_id={message_id}"

    response = requests.post(url_chat, json={"offset": None, "limit": None, "timeout": 25})
    parsed_response = json.loads(response.text)
    print(json.dumps(parsed_response, indent=8))


# delete_message(api_url=api_url, chat_id=api_chat_id, message_id='676')


def get_me(api_url):
    url_chat = f"{api_url}/getMe"

    response = requests.post(url_chat)
    parsed_response = json.loads(response.text)
    print(json.dumps(parsed_response, indent=8))

    # https://stackoverflow.com/questions/61976560/how-to-delete-queue-updates-in-telegram-api

def get_updates(api_url):
    url_chat = f"{api_url}/getUpdates"

    response = requests.post(url_chat, json={"offset": -1, "limit": None, "timeout": None})
    parsed_response = json.loads(response.text)
    print(json.dumps(parsed_response, indent=8))

    # get_updates(api_url=api_url)


def send_message_to_user_by_login(api_url, from_chat_id, message_id, chat_id):
    url_chat = f"{api_url}/forwardMessage?from_chat_id={from_chat_id}&message_id={message_id}&chat_id={chat_id}"

    response = requests.post(url_chat, json={"offset": -1, "limit": None, "timeout": None})
    parsed_response = json.loads(response.text)
    print(json.dumps(parsed_response, indent=8))


send_message_to_user_by_login(api_url=api_url,from_chat_id=api_chat_id, message_id='677', chat_id='6157282833')