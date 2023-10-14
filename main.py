from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

username = "telemetr.obucheniye@mail.ru"
password = "obuchTG123"

about = '%D0%BF%D1%81%D0%B8%D1%85%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D1%8F'
views_post_from = 1000
views_post_to = 2000
mentions_week_from = 1
er_from = 8
er_to = 20
title = '%D0%BF%D1%81%D0%B8%D1%85%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D1%8F'
link = f'https://telemetr.me/channels/?title={title}&about={about}&views_post_from={views_post_from}&views_post_to={views_post_to}&mentions_week_from={mentions_week_from}&er_from={er_from}&er_to={er_to}&lang_code=any'


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
time.sleep(1)

driver.get(link)

page_source_html = driver.page_source
soup = BeautifulSoup(page_source_html, 'lxml')
td_arr = soup.find_all('td', class_='text-center wd-100 pb-0')
pag_ul = soup.find('ul', class_='kt-pagination__links')
pag_li_arr = pag_ul.find_all('li')
# print(pag_li_arr[-1].text)
count = int(pag_li_arr[-1].text)

links_arr = []
for i in range(1, 2):
# for i in range(1, count+1):
    links_arr.append(f'{link}&page={i}')
# print(links_arr)


chanal_arr = []
for link in links_arr:
    driver.get(link)
    # print(link)

    html_link = driver.page_source
    soup_link = BeautifulSoup(html_link, 'lxml')
    td_arr = soup_link.find_all('td', class_='text-center wd-100 pb-0')
    # print(len(td_arr))

    for j, td in enumerate(td_arr):
        link = td.find("a")
        href = link.get("href")
        chanal_arr.append(href)
        print(j, href)


    time.sleep(1)

with open('chanal_arr.txt', 'w') as f:
    for line in chanal_arr:
        f.write(f"{line}\n")
# 0 /@teacher_korea

