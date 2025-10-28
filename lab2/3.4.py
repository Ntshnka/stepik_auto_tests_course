import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/alert_accept.html")

try:
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    WebDriverWait(browser, 5).until(EC.alert_is_present())
    alert = browser.switch_to.alert
    alert.accept()

    x_element = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "input_value"))
    )
    x = x_element.text
    y = calc(x)

    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    result_alert = WebDriverWait(browser, 5).until(EC.alert_is_present())
    result_text = result_alert.text
    print("Ответ:", result_text.split()[-1])
    result_alert.accept()

    time.sleep(5)

finally:
    browser.quit()