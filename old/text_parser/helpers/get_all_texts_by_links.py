import json
from old.text_parser.helpers.get_one_text_by_llink import get_text_by_link
from old.text_parser.settings import sub_theme
from old.text_parser.helpers.set_folders import folders_names


def get_all_texts_by_links():
    path = folders_names['links']
    f = open(f'{path}/{sub_theme}.json')
    data = json.load(f)

    for i in data:
        # if i == "1":
        get_text_by_link(data[i]['link'])
        # update_json_file(f'{path}/links_in.json', i, 'is_text', True)
        # update_json_file(f'{path}/links_in.json', i, 'is_translate', True)
        print(data[i]['link'])

    f.close()
