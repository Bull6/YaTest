import pytest

import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

'''chromedriver = "./chromedriver"

driver = webdriver.Chrome(chromedriver)

driver.implicitly_wait(5)

driver.get("https://yandex.ru")'''


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome("./chromedriver")
    yield driver
    driver.quit()

def test_Textbox(browser):
    browser.get("https://yandex.ru")
    #locator = (By.CSS_SELECTOR,'.search2__input')
    locator = (By.ID, 'text')
    timeout = 10
    elements = WebDriverWait(browser, timeout).until(EC.visibility_of_element_located(locator))
    assert elements

def test_Suggest(browser):


    browser.find_element_by_id('text').send_keys('Тензор')

    locator = (By.CSS_SELECTOR, '.mini-suggest__popup.mini-suggest__popup_theme_flat.mini-suggest__popup_visible')
    timeout = 10
    elements = WebDriverWait(browser, timeout).until(EC.visibility_of_element_located(locator))
    assert elements


def test_TableSearch(browser):


    browser.find_element_by_id('text').send_keys('\n')

    locator = (By.CSS_SELECTOR, '.content__left')
    timeout = 10
    elements = WebDriverWait(browser, timeout).until(EC.visibility_of_element_located(locator))
    assert elements


def test_Top5Tensor(browser):

    urls = browser.find_elements_by_css_selector('.OrganicTitle-Link')
    results = []
    for url in urls[:5]:
        results.append(url.get_attribute("href"))
    res = list(filter(lambda x: 'tensor.ru' in x, results))

    assert len(res) > 0


