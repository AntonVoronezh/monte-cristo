import time
import math
from datetime import date, datetime
from random import choice
from threading import Event

from colorama import Fore


def ff():
    print('выполнение переданной функции')


current_date = date.today()


# https://pythonru.com/primery/kak-ispolzovat-modul-datetime-v-python

def print_sleep(a, b, format):  # в минутах
    r = range(a, b)
    t = choice(r)

    print(f'{t} {format} ждем', end='')

    for i, _ in enumerate(range(1, t)):
        if format == 'sec':
            time.sleep(1)
        if format == 'min':
            time.sleep(60)

        if i == t - 2:
            print(f'.', end='\n', flush=True)
        else:
            print(f'.', end='', flush=True)


def post_timer(func):
    # print(current_date)
    func()
    current_time = datetime.now().time()
    current_time_split = str(current_time).split('.')
    print(Fore.BLUE + f'{current_time_split[0]}' + Fore.RESET)
    print_sleep(a=10, b=30, format='sec')
    post_timer(func)


post_timer(ff)
