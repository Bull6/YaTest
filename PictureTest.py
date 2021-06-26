import pytest
import pytest_html
import time
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome("./chromedriver")
    yield driver
    driver.quit()

def test_PicIcon(browser):
    browser.get("https://yandex.ru")
    link = browser.find_element_by_link_text('Картинки')
    browser.set_page_load_timeout(10)
    link.click()
    browser.switch_to.window(browser.window_handles[1])

    url = browser.current_url

    assert "https://yandex.ru/images/" in url

def test_Top1Pics(browser):

    link = browser.find_element_by_css_selector('.PopularRequestList-Shadow')
    link_text = link.text
    browser.set_page_load_timeout(10)
    link.click()

    current_text = browser.find_element_by_class_name('input__control').text
    time.sleep(2)
    assert link_text == current_text



def test_OpenPic(browser):
    link = browser.find_element_by_css_selector('.serp-item')
    
    browser.set_page_load_timeout(10)
    link.click()

    locator = (By.CSS_SELECTOR, '.MMImageWrapper')
    timeout = 10  # время ожидания
    elements = WebDriverWait(browser, timeout).until(EC.visibility_of_element_located(locator))

    assert elements

def test_NextPic(browser):
    global pic1
    pic1 = browser.find_element_by_class_name('MMImage-Origin').get_attribute('src')
    #pic1 = driver.current_url

    browser.set_page_load_timeout(10)

    nextpic = browser.find_element_by_css_selector('.MediaViewer-ButtonNext')
    nextpic.click()

    pic2 = browser.find_element_by_class_name('MMImage-Origin').get_attribute('src')
    #pic2 = driver.current_url

    assert pic1 != pic2

def test_PrevPic(browser):

    browser.set_page_load_timeout(10)

    prevpic = browser.find_element_by_css_selector('.MediaViewer-ButtonPrev')
    prevpic.click()

    pic = browser.find_element_by_class_name('MMImage-Origin').get_attribute('src')

    assert pic1 == pic
