import json


def get_title_and_caption(file):
    data = json.load(file)
    title = data['title']
    description = data['description']

    return {"title": title, 'description': description}
