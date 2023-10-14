import fake_useragent
import requests
from bs4 import BeautifulSoup
import lxml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
def get_data_with_selenium(url):

    # ua = fake_useragent.UserAgent()
    # fake_ua = {'user-agent': ua.random}
    # response = requests.get(url=url, headers=fake_ua)
    # response.encoding = 'utf-8'
    # soup = BeautifulSoup(response.text_for_msg, 'lxml')
    # print(soup)
    # link_latest = soup.find('button', class_='btn btn-custom')
    brouzer = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    brouzer.get(url)

    # my_div = brouzer.find_element(By.CLASS_NAME, 'affix-top')
    # print(my_div.get_attribute("outerHTML"))
    button = brouzer.find_element(By.ID, 'load_more_stories')
    button.click()
    time.sleep(10)
    button.click()
    time.sleep(10)
    # fa - ul list - padded
    my_div = brouzer.find_element(By.TAG_NAME, 'html')
    print(my_div.get_attribute("outerHTML"))
    # # brouzer.execute_script("arguments[0].click();", button)
    # time.sleep(2)
    brouzer.quit()

get_data_with_selenium('https://www.sciencedaily.com/news/health_medicine/colitis')
# get_data_with_selenium('https://pythonexamples.org/tmp/selenium/index-50.html')

