import math
from datetime import datetime

from colorama import Fore
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

from helpers.get_data_table import get_data_table
from helpers.get_reklama import get_advertising_count
from helpers.get_total_info import get_total_info
from helpers.get_data_table_info import get_data_table_info
from helpers.get_renames import get_renames
from helpers.save_xlsx import save_xlsx
from settings.chanel_data_settings import danger_link_setting, advertising_count_setting

start_time = datetime.now()

username = "telemetr.obucheniye@mail.ru"
password = "obuchTG123"
link = f'https://telemetr.me'

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://telemetr.me/login/")
time.sleep(1)
driver.refresh()
time.sleep(1)

driver.find_element(By.XPATH, "//input[@name='login[email]']").send_keys(username)
driver.find_element(By.XPATH, "//input[@name='login[password]']").send_keys(password)
driver.find_element(By.XPATH, "//button[@name='do_login']").click()

with open('chanal_arr.txt') as f:
    chanal_arr = f.readlines()
# print(current)

total_info_arr = []

for i, row in enumerate(chanal_arr):
    chanel_name = row.replace('\n', '')
    current_link = f'{link}{chanel_name}'

    # if i == 0:
    if i < 100:
        print(f'{i + 1} из {len(chanal_arr)}, {chanel_name}', flush=True, end='')
        driver.get(current_link)
        # print(link)
        advertising_count = get_advertising_count(driver=driver)
        if advertising_count > advertising_count_setting:
            print(Fore.RED + f'много рекламы в день {advertising_count}' + Fore.RESET)

        current_total_info = get_total_info(driver=driver, current_link=current_link, chanel_name=chanel_name)
        if current_total_info is not None:
            data_table = get_data_table(driver=driver)
            if data_table is not None:
                danger_link_count = data_table[1]
                if danger_link_count > danger_link_setting:
                    print(Fore.RED + f'много плохих ссылок {danger_link_count}' + Fore.RESET)


                else:
                    all_link_count = data_table[0]

                    new_current_total_info = []

                    for el in current_total_info:
                        new_current_total_info.append(el)

                    new_current_total_info.append(all_link_count)
                    new_current_total_info.append(danger_link_count)
                    total_info_arr.append(new_current_total_info)

        # driver.find_element(By.XPATH, "//a[@data-do='show_modal_title_history']").click()
        # time.sleep(5)
        # # renames_arr = driver.find_element(By.XPATH, "//div[@id='modal_title_history']").find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
        # driver.find_element(By.XPATH, "//button[@data-dismiss='modal']")
        # driver.execute_script("arguments[0].click();", ele)
        # driver.close()
        # driver.switch_to.window(parent_window)

save_xlsx(total_info_arr)

lambda_ = datetime.now() - start_time
lambda_sec = lambda_.total_seconds()
lambda_sec_out = f'{math.ceil(lambda_sec)} секунд' if lambda_sec < 60 else f'{math.ceil(lambda_sec / 60)} минут'

print(Fore.BLUE + f'\n время выполнения - {lambda_sec_out}' + Fore.RESET)
