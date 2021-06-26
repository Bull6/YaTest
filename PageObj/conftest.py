import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome("./../chromedriver")
    yield driver
    driver.quit()