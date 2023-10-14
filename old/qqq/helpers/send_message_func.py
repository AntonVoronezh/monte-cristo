import requests
import json
import os


def save_result(response, chat_id, messages_type):
    script_dir = os.path.dirname(__file__).replace('\helpers', '')
    # test = open(f'{script_dir}/result/messages_id.txt', 'a')
    # test.write(f'{response["result"]["message_id"]}\n')
    # test.close()
    print(response)
    new_message = [
        {
            'id': response["result"]["message_id"],
            'messages_type': messages_type
        }
    ]

    path = os.path.join(script_dir, 'results', 'results.json')

    if not os.path.exists(path):
        json_result = {
            'chanel_id': chat_id,
            'chanel_name':  response["result"]['sender_chat']["title"],
            'username':  response["result"]['sender_chat']["username"],
            'messages': new_message
        }
        with open(path, 'w') as outfile:
            json.dump(json_result, outfile, indent=4)
    else:
        json_file = open(path, "r")
        data = json.load(json_file)
        json_file.close()

        data['messages'] = data['messages'] + new_message

        json_file = open(path, "w+")
        json_file.write(json.dumps(data, indent=4))
        json_file.close()


def parsed_response(url_message, files={}):
    try:
        response = requests.post(url_message, files=files)
        return json.loads(response.text)
    except Exception as e:
        print(e)


def get_updates(url):
    url_chat = f"{url}/getUpdates"

    response = requests.post(url_chat, json={"offset": None, "limit": None, "timeout": 25})
    parsed_response = json.loads(response.text)
    print(json.dumps(parsed_response, indent=8))


def send_message(message, api_url, chat_id):
    url_message = f"{api_url}/sendMessage?chat_id={chat_id}&text={message}&parse_mode=html"
    return parsed_response(url_message)


def send_big_message(message, api_url, chat_id):
    if len(message) > 4096:
        for x in range(0, len(message), 4096):
            return send_message(message[x:x + 4096], api_url, chat_id)
    else:
        return send_message(message, api_url, chat_id)


# def send_image_from_url(image, url, chat_id):
#     url_message = f"{url}/sendPhoto"
#
#     try:
#         response = requests.post(url_message, json={'chat_id': chat_id, 'photo': image})
#         parsed_response = json.loads(response.text_for_msg)
#         print(json.dumps(parsed_response, indent=8))
#     except Exception as e:
#         print(e)



def send_photo_from_file(api_url, chat_id, file_opened, caption=''):
    url_message = f"{api_url}/sendPhoto?chat_id={chat_id}&caption={caption}"
    files = {'photo': file_opened}
    return parsed_response(url_message, files)


def send_photo_group_from_file(api_url, chat_id, file_opened_arr):
    media = []
    files = {}

    for file_opened in file_opened_arr:
        # media.append(dict(type='photo', media=f'attach://{file_opened}'))
        media.append(dict(type='photo', media=f'attach://../img/1111.jpg'))
        files[file_opened] = open(file_opened, 'rb')
    print(json.dumps(media))
    url_message = f"{api_url}/sendMediaGroup?chat_id={chat_id}&media={json.dumps(media)}"

    return parsed_response(url_message, files)


def send_audio_from_file(api_url, chat_id, file_opened, caption=''):
    url_message = f"{api_url}/sendAudio?chat_id={chat_id}&caption={caption}"
    files = {'audio': file_opened}
    return parsed_response(url_message, files)


def send_document_from_file(api_url, chat_id, file_opened, caption=''):
    url_message = f"{api_url}/sendDocument?chat_id={chat_id}&caption={caption}"
    files = {'document': file_opened}
    return parsed_response(url_message, files)


def send_poll(api_url, chat_id, poll):
    json_poll = json.load(poll)
    url_message = f"{api_url}/sendPoll?chat_id={chat_id}&question={json_poll['question']}&options={json.dumps(json_poll['options'])}&is_anonymous={True}"
    return parsed_response(url_message)


def send_quiz(api_url, chat_id, poll):
    json_poll = json.load(poll)
    url_message = f"{api_url}/sendPoll?type=quiz&chat_id={chat_id}&question={json_poll['question']}&options={json.dumps(json_poll['options'])}&is_anonymous={True}&correct_option_id={json_poll['correct_option_id']}"
    return parsed_response(url_message)


def send_repost_message(url, chat_id, from_chat_id, message_id):
    url_message = f"{url}/forwardMessage?chat_id={chat_id}&from_chat_id={from_chat_id}&message_id={message_id}"
    return parsed_response(url_message)
