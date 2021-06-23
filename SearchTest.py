import pytest
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from selenium import webdriver
#import chromedriver_binary  # Adds chromedriver binary to path

chromedriver = "C:/Users/DenT/Downloads/chromedriver.exe"
driver = webdriver.Chrome(chromedriver)
# https://selenium-python.readthedocs.io/waits.html#implicit-waits
driver.implicitly_wait(5)

driver.get("https://yandex.ru")

def setup_module(module):
    # init_something()
    pass


def teardown_module(module):
    # teardown_something()
    pass


def test_Textbox():
    locator = (By.CSS_SELECTOR,
               '.search2__input')  # просто пример, необходимо вставить свое значение
    timeout = 10  # время ожидания
    elements = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))
    assert elements

def test_Suggest():

    # Вводим текст в поле для поиска
    driver.find_element_by_id('text').send_keys('Тензор')

    locator = (By.CSS_SELECTOR, '.mini-suggest__popup.mini-suggest__popup_theme_flat.mini-suggest__popup_visible')  # просто пример, необходимо вставить свое значение
    timeout = 10  # время ожидания
    elements = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))
    assert elements


def test_TableSearch():

    # Вводим текст в поле для поиска
    driver.find_element_by_id('text').send_keys('\n')

    locator = (By.CSS_SELECTOR, '.content__left')  # просто пример, необходимо вставить свое значение
    timeout = 10  # время ожидания
    elements = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))
    assert elements


def test_Top5Tensor():

    #driver.find_element_by_id('text').send_keys('Тензор\n')

    # Ищем элементы <span class="suggest2-item__text">
    #urls = driver.find_elements_by_class_name('Link Link_theme_normal OrganicTitle-Link OrganicTitle-Link_wrap Typo Typo_text_l Typo_line_m organic__url link i-bem link_js_inited')
    urls = driver.find_elements_by_partial_link_text("tensor")
    results = []
    for url in urls:
        results.append(url.get_attribute("href"))
    res = list(filter(lambda x: 'tensor.ru' in x, results))



    assert len(res) > 5

    #assert len(suggestions) > 0
    driver.close()

