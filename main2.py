from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
from save_xlsx import save_xlsx

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

for i, row in enumerate(chanal_arr):
    row_split = row.replace('\n', '')
    current_link = f'{link}{row_split}'

    if i == 0:
        print(row_split)
        driver.get(current_link)
        # print(link)

        html_link = driver.page_source
        soup_link = BeautifulSoup(html_link, 'lxml')
        name = soup_link.find('a', class_='kt-widget__username').text.strip()
        desc = soup_link.find('div', class_='kt-widget__desc t_long').text.strip()
        participants = soup_link.find("span", attrs={"data-num": "participants"}).text.strip().replace("'", "")
        participants_today = soup_link.find("span", attrs={"data-num": "participants_today"}).text.strip().replace("'",
                                                                                                                   "")
        participants_week = soup_link.find("span", attrs={"data-num": "participants_week"}).text.strip().replace("'",
                                                                                                                 "")
        views_per_post = soup_link.find("span", attrs={"data-num": "views_per_post"}).text.strip().replace("'", "")
        # print(name)
        # print(desc)
        # print(participants)
        # print(participants_today)
        # print(participants_week)
        # print(participants_month)
        er_per_post = soup_link.find("span", attrs={"data-num": "er_per_post"}).text.strip().replace("%", "")
        er_24 = soup_link.find("span", attrs={"data-num": "er_24"}).text.strip().replace("%", "")

        # print(er_per_post)
        # print(er_24)

        p_cpm = 300
        data_views_subs = soup_link.find("span", class_='kt-number kt-font-brand text-underlined')
        p_views = data_views_subs.get('data-views')
        p_subs = data_views_subs.get('data-subs')
        p_summ = round((p_cpm / 1000) * int(p_views))
        p_pdp = round(100 * p_summ / int(p_subs)) / 100

        mentions_count = data_views_subs.text.strip().replace("'", "")
        reposts_count = soup_link.find("span", class_='kt-number kt-font-brand').text.strip().replace("'", "")

        # save_xlsx(
        #     name=name,
        #     current_link=current_link,
        #     row_split=row_split,
        #     desc=desc,
        #     participants=participants,
        #     views_per_post=views_per_post,
        #     er_per_post=er_per_post,
        #     p_pdp=p_pdp,
        #     mentions_count=mentions_count,
        #     reposts_count=reposts_count
        # )

        data_tables_div = driver.find_element(By.CLASS_NAME, 'dataTables_scrollBody')
        ActionChains(driver).scroll_to_element(data_tables_div).perform()

        all_elements = driver.find_elements(By.CSS_SELECTOR, 'div.dataTables_scrollBody > table > tbody > tr')
        print(len(all_elements), all_elements[0].text)
        print(len(all_elements), all_elements[1].text)
        print(len(all_elements), all_elements[2].text)
        print(len(all_elements), all_elements[3].text)
        print(len(all_elements), all_elements[4].text)
        last_element = None
        # for i, _ in enumerate(range(1, 10)):
        # while True:
        #     driver.execute_script("arguments[0].scrollBy(0, arguments[0].scrollHeight);", data_tables_div)
        #     time.sleep(1)
        #     all_elements = driver.find_elements(By.CSS_SELECTOR, 'div.dataTables_scrollBody > table > tbody > tr')
        #     print(len(all_elements), all_elements[0].text)
        #     if all_elements[-1] == last_element:
        #         break
        #     else:
        #         last_element = all_elements[-1]

            # html_data_table = driver.page_source
            # soup_data_table = BeautifulSoup(html_data_table, 'lxml')
            # table_who_mentioned = soup_data_table.find('table', id='who_mentioned')
            # tr_arr_even = soup_data_table.find_all('tr', class_='even')
            # tr_arr_odd = soup_data_table.find_all('tr', class_='odd')
            # print(i)
            # print(len(tr_arr_even), tr_arr_even[0].text)
            # print(len(tr_arr_odd), tr_arr_odd[0].text)
            # print(len(rows_arr), flush=True)
        # print(len(rows_arr))
        # print(len(tr_arr))
        # for i in tr_arr:
        #     print(i)
        #     # span = i.find('span', class_='kt - number')
        #     # print(span.text, flush=True)
