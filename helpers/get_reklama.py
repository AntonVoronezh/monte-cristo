import math

from selenium.webdriver.common.by import By


def get_advertising_count(driver):
    driver.find_element(By.XPATH, "//a[@href='#tab_all_efficiency']").click()
    all_elements = driver.find_elements(By.XPATH, "//div[@class='kt-portlet__body p-4']")

    for el in all_elements:
        if 'За неделю' in el.text:
            arr = el.text.split('\n')
            count = int(arr[1].strip())
            average_count = math.floor(count/7)

            return average_count

    return 0