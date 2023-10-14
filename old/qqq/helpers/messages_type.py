import os
from random import choice


def get_next_message_type():
    folders_path = os.path.dirname(os.path.realpath(__file__).replace('\helpers', ''))

    def check_folders(name):
        if len(name.split('.')) == 2 or name == 'helpers' or name == 'results':
            return False
        return True

    folder_list = list(filter(check_folders, os.listdir(folders_path)))
    messages_types = []
    # print(folder_list)
    for name in folder_list:
        d = os.listdir(os.path.join(folders_path, name))

        if len(d) != 0:
            messages_types.append(name)

    if len(messages_types) == 0:
        return None

    f = open(os.path.join(folders_path, 'results', 'message_type.txt'), 'r')
    last_messages_type = f.read()
    f.close()
    last_messages_type_index = 0
    try:
        last_messages_type_index = messages_types.index(last_messages_type)
    except:
        messages_types.index(choice(messages_types))

    next_messages_type_index = last_messages_type_index + 1 if last_messages_type_index + 1 <= len(
        messages_types) - 1 else 0
    next_messages_type = messages_types[next_messages_type_index]
    ff = open(os.path.join(folders_path, 'results', 'message_type.txt'), 'w')
    ff.write(next_messages_type)
    ff.close()

    return next_messages_type;
