import math

from bs4 import BeautifulSoup
from colorama import Fore

from settings.chanel_data_settings import sub_cost_setting, participants_month_plus_setting, mentions_count_setting, \
    reposts_count_setting, cpm_setting


def get_total_info(driver, current_link, chanel_name):
    html = driver.page_source
    soup_link = BeautifulSoup(html, 'lxml')
    name = soup_link.find('a', class_='kt-widget__username').text.strip()
    desc = soup_link.find('div', class_='kt-widget__desc t_long').text.strip()
    participants = soup_link.find("span", attrs={"data-num": "participants"}).text.strip().replace("'", "")
    participants_today = soup_link.find("span", attrs={"data-num": "participants_today"}).text.strip().replace("'",
                                                                                                              "")
    participants_week = soup_link.find("span", attrs={"data-num": "participants_week"}).text.strip().replace("'",
                                                                                                             "")
    participants_month = soup_link.find("div", id='new_week').find_all('span')[1].text.strip()

    views_per_post = soup_link.find("span", attrs={"data-num": "views_per_post"}).text.strip().replace("'", "")
    er_per_post = soup_link.find("span", attrs={"data-num": "er_per_post"}).text.strip().replace("%", "")
    er_24 = soup_link.find("span", attrs={"data-num": "er_24"}).text.strip().replace("%", "")


    data_views_subs = soup_link.find("span", attrs={"data-do": 'show_days_mentions'})
    p_views = data_views_subs.get('data-views')
    p_subs = data_views_subs.get('data-subs')
    p_summ = round((cpm_setting / 1000) * int(p_views))
    p_pdp = round(100 * p_summ / int(p_subs)) / 100

    mentions_count = data_views_subs.text.strip().replace("'", "")
    reposts_count = soup_link.find('span', attrs={"data-original-title": 'Репостов'}).text.strip().replace("'", "")
    tg_link = chanel_name.replace('@', '')

    advertising_cost =math.ceil(( int(views_per_post) * cpm_setting) / 1000)

    if '@' not in desc:
        print(Fore.RED + f' нет контактных данных' + Fore.RESET)
        return None
    if participants_month_plus_setting and '+' not in participants_month:
        print(Fore.RED + f' минус по подписчикам за месяц {participants_month}' + Fore.RESET)
        return None
    if int(mentions_count) < mentions_count_setting:
        print(mentions_count_setting, int(mentions_count))
        print(Fore.RED + f' мало упоминаний {mentions_count}' + Fore.RESET)
        return None
    if int(reposts_count) < reposts_count_setting:
        print(Fore.RED + f' мало репостов {reposts_count}' + Fore.RESET)
        return None
    if sub_cost_setting > p_pdp:
        print(Fore.RED + f' цена подписчика меньше {sub_cost_setting}' + Fore.RESET)
        return None
    else:
        print(Fore.GREEN + f' параметры подошли' + Fore.RESET)
        return ['', '', name, '', current_link, f'http://t.me{tg_link}', desc, participants, views_per_post, er_per_post,
            p_pdp, mentions_count, reposts_count, advertising_cost]
