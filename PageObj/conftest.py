import pytest
import pytest_html
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome("./../chromedriver")
    yield driver
    driver.quit()