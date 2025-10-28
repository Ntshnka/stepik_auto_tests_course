import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

try:
    price_wait = WebDriverWait(browser, 15)
    price_wait.until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()

    result_alert = WebDriverWait(browser, 10).until(EC.alert_is_present())
    result_text = result_alert.text
    print("Ответ:", result_text.split()[-1])
    result_alert.accept()

    time.sleep(2)

finally:
    browser.quit()