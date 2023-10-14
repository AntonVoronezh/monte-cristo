from colorama import Fore

import time

from datetime import datetime
from random import choice

def print_sleep(a, b, format):  # в минутах
    r = range(a, b)
    t = choice(r)

    print(f'{t} {format} ждем', end='', flush=True)

    for i, _ in enumerate(range(1, t)):
        if i == t - 2:
            print(f'.', end='\n', flush=True)
        else:
            print(f'.', end='', flush=True)

        if format == 'sec':
            time.sleep(1)
        if format == 'min':
            time.sleep(60)


def post_timer(func):
    func()
    current_time = datetime.now().time()
    current_time_split = str(current_time).split('.')
    print(Fore.BLUE + f'{current_time_split[0]}' + Fore.RESET)
    print_sleep(a=100, b=120, format='min')
    post_timer(func)

