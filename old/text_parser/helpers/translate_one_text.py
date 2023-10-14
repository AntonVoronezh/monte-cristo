import json
from googletrans import Translator
from old.text_parser.helpers.set_folders import folders_names


def translate_one_text(name):
    translator = Translator()

    path = folders_names['text_for_msg']
    f = open(f'{path}/{name}.json')
    data = json.load(f)

    json_result = {
        'title': translator.translate(data['title'], dest='ru').text,
        'summary': translator.translate(data['summary'], dest='ru').text,
        'first': translator.translate(data['first'], dest='ru').text,
        'text_for_msg': []
    }

    for txt in data['text_for_msg']:
        txt_ru = translator.translate(txt, dest='ru')
        json_result['text_for_msg'].append(txt_ru.text)

    path = folders_names['translate']
    with open(f"{path}/{name}.json", 'w', encoding='utf-8') as outfile:
        json.dump(json_result, outfile, indent=4, ensure_ascii=False)

    print(name)
