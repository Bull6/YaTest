import pytest

import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

chromedriver = "./chromedriver.exe"

driver = webdriver.Chrome(chromedriver)

driver.implicitly_wait(5)

driver.get("https://yandex.ru")



def test_Textbox():
    #locator = (By.CSS_SELECTOR,'.search2__input')
    locator = (By.ID, 'text')
    timeout = 10  # время ожидания
    elements = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))
    assert elements

def test_Suggest():

    # Вводим текст в поле для поиска
    driver.find_element_by_id('text').send_keys('Тензор')

    locator = (By.CSS_SELECTOR, '.mini-suggest__popup.mini-suggest__popup_theme_flat.mini-suggest__popup_visible')
    timeout = 10  # время ожидания
    elements = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))
    assert elements


def test_TableSearch():

    # Вводим текст в поле для поиска
    driver.find_element_by_id('text').send_keys('\n')

    locator = (By.CSS_SELECTOR, '.content__left')
    timeout = 10  # время ожидания
    elements = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))
    assert elements


def test_Top5Tensor():


    # Ищем элементы <span class="suggest2-item__text">
    urls = driver.find_elements_by_partial_link_text("tensor")
    results = []
    for url in urls:
        results.append(url.get_attribute("href"))
    res = list(filter(lambda x: 'tensor.ru' in x, results))

    assert len(res) > 5



