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

pic1 = ''

def test_PicIcon():

    link = driver.find_element_by_link_text('Картинки')
    driver.set_page_load_timeout(10)
    link.click()
    driver.switch_to.window(driver.window_handles[1])

    url = driver.current_url

    assert "https://yandex.ru/images/" in url

def test_Top1Pics():

    link = driver.find_element_by_css_selector('.PopularRequestList-Shadow')
    link_text = link.text
    driver.set_page_load_timeout(10)
    link.click()

    current_text = driver.find_element_by_class_name('input__control').text

    assert link_text == current_text

def test_OpenPic():
    link = driver.find_element_by_css_selector('.serp-item__preview')
    link_text = link.text
    driver.set_page_load_timeout(10)
    link.click()

    locator = (By.CSS_SELECTOR, '.MMImageWrapper')
    timeout = 10  # время ожидания
    elements = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))

    assert elements

def test_NextPic():
    global pic1
    pic1 = driver.find_element_by_class_name('MMImage-Origin').get_attribute('src')
    #pic1 = driver.current_url

    driver.set_page_load_timeout(10)

    nextpic = driver.find_element_by_css_selector('.MediaViewer-ButtonNext')
    nextpic.click()

    pic2 = driver.find_element_by_class_name('MMImage-Origin').get_attribute('src')
    #pic2 = driver.current_url

    assert pic1 != pic2

def test_PrevPic():

    driver.set_page_load_timeout(10)

    prevpic = driver.find_element_by_css_selector('.MediaViewer-ButtonPrev')
    prevpic.click()

    pic = driver.find_element_by_class_name('MMImage-Origin').get_attribute('src')

    assert pic1 == pic
    driver.quit()
