import requests
import json
import os


def post_messages_by_list():
    script_dir = os.path.dirname(__file__).replace('telegram', f'text_parser\\links\\colitis.json')
    print(script_dir)
    f = open(script_dir)
    data = json.load(f)

    for i in data:
        # update_json_file(f'{path}/links_in.json', i, 'is_text', True)
        # update_json_file(f'{path}/links_in.json', i, 'is_translate', True)
        print(data[i])

    f.close()


post_messages_by_list()
