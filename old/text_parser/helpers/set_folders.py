import os
from old.text_parser.settings import sub_theme

folders_names = {
    'script_dir': '',
    'links': '',
    'text_for_msg': '',
    'sub_theme': '',
    'translate': ''
}


def set_folders():
    script_dir = os.path.dirname(__file__).replace('\helpers', '')
    folders_names['links'] = 'links'
    folders_names['text_for_msg'] = 'text_for_msg';
    folders_names['translate'] = 'translate';
    folders_names['sub_theme'] = os.path.join(script_dir, folders_names['text_for_msg'], sub_theme)
    folders_names['translate_sub_theme'] = os.path.join(script_dir, folders_names['translate'], sub_theme)

    if not os.path.exists(folders_names['translate']):
        os.mkdir(folders_names['translate'])

    if not os.path.exists(folders_names['text_for_msg']):
        os.mkdir(folders_names['text_for_msg'])

    if not os.path.exists(folders_names['links']):
        os.mkdir(folders_names['links'])
