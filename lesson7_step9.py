from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
# import os
import math


def calc(x: str):
    return str(math.log(abs(12 * math.sin(int(x)))))


if __name__ == "__main__":
    try:
        link1 = " http://suninjuly.github.io/explicit_wait2.html"
        browser1 = webdriver.Chrome()
        browser1.get(link1)

        # Ваш код, который заполняет обязательные поля

        WebDriverWait(browser1, 12).until(ec.text_to_be_present_in_element((By.ID, "price"), "$100"))

        button = browser1.find_element(By.ID, "book")
        button.click()

        x = browser1.find_element(By.ID, "input_value").text
        answer = browser1.find_element(By.ID, "answer")
        browser1.execute_script("return arguments[0].scrollIntoView(true);", answer)
        answer.send_keys(str(calc(x)))

        button = browser1.find_element(By.ID, "solve")
        browser1.execute_script("return arguments[0].scrollIntoView(true);", button)
        button.click()

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser1.quit()
