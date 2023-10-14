import os
from b1_helpers.main import check_folders_main
from b1_helpers.time import post_timer

from a0_proba.main import start as a0_proba_start
from a1_doctor_psyh.main import start as a1_doctor_psyh_start

is_develop = False


def main():
    realpath = os.path.dirname(os.path.realpath(__file__))

    if is_develop:
        projects = ['a0_proba']
    else:
        folder_list = os.listdir(realpath)
        projects = list(filter(check_folders_main, folder_list))

    if len(projects) == 0:
        print(f'🔴 нет проектов')
        return

    else:
        for project in projects:
            if project == 'a0_proba':
                a0_proba_start()
            if project == 'a1_doctor_psyh':
                a1_doctor_psyh_start()


post_timer(main)
