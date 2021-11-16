from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 15)


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    # Открыть страницу http://suninjuly.github.io/explicit_wait2.html
    browser.get('http://suninjuly.github.io/explicit_wait2.html')

    # Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    wait.until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))

    # Нажать на кнопку "Book"
    browser.find_element_by_id('book').click()

    # Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
    x = browser.find_element_by_id('input_value').text
    result = calc(int(x))

    browser.find_element_by_id('answer').send_keys(result)
    browser.find_element_by_id('solve').click()

finally:
    time.sleep(10)
    browser.quit()