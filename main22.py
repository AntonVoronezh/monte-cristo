from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

username = "telemetr.obucheniye@mail.ru"
password = "obuchTG123"
link = f'https://telemetr.me'

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
# driver = webdriver.Firefox()

driver.get(link)
# driver.find_element(By.XPATH, "//input[@name='login[email]']").
# data_tables_div = soup_link.find("div", id='dataTables_scrollBody')
# driver.execute_script("window.scrollBy(0,2000)", "")
# data_tables_div = driver.find_element(By.CSS_SELECTOR, 'div.scroll-container_1')
# page_source_html = driver.page_source
# print(data_tables_div.text)
ActionChains(driver).scroll_to_element(driver.find_element(By.ID, "dataTables_scrollBody")).perform()
# time.sleep(3)

# ActionChains(driver).scroll_to_element(data_tables_div).perform()
for x in range(10):
    #     print(x)
    # while True:
    driver.execute_script("arguments[0].scrollBy(0, arguments[0].scrollHeight);", data_tables_div)
    time.sleep(2)

    ActionChains(driver).move_to_element(data_tables_div).scroll_by_amount(1,1500).perform()

data_tables_div_2 = driver.find_element(By.CLASS_NAME, 'dataTables_scrollBody')
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", data_tables_div)
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", data_tables_div_2)
driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", data_tables_div_2)
counter = 0
for _ in range(8):
    data_tables_div_2.execute_script("window.scrollBy(0, arguments[0]);", counter)
    counter += 1000
    time.sleep(2)



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

