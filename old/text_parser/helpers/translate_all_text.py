import json
from old.text_parser.settings import sub_theme
from old.text_parser.helpers.set_folders import folders_names
from old.text_parser.helpers.translate_one_text import translate_one_text


def translate_all_text():
    path = folders_names['links']
    f = open(f'{path}/{sub_theme}.json')
    data = json.load(f)

    for i in data:
        # get_text_by_link(data[i]['link'])
        # update_json_file(f'{path}/links_in.json', i, 'is_text', True)
        # update_json_file(f'{path}/links_in.json', i, 'is_translate', True)
        translate_one_text(data[i]['name'])

    f.close()
