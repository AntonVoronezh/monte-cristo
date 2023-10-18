# pip install zenrows
import time

from selenium.webdriver.common.by import By
from zenrows import ZenRowsClient
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

client = ZenRowsClient("728afbf03652fcc8b00239af56aef675524b064b")
url = "https://telemetr.me/channels/"
params = {"js_render":"true","antibot":"true"}

response = client.get(url, params=params)
link = f'https://telemetr.me/@butlin'
username = "telemetr.obucheniye@mail.ru"
password = "obuchTG123"
#
# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=chrome_options)
#
# driver.get("https://telemetr.me/login/")
# time.sleep(1)
# driver.refresh()
# time.sleep(1)
# driver.find_element(By.XPATH, "//input[@name='login[email]']").send_keys(username)
# driver.find_element(By.XPATH, "//input[@name='login[password]']").send_keys(password)
# driver.find_element(By.XPATH, "//button[@name='do_login']").click()
# time.sleep(1)
#
# driver.get(link)

print(response.text)