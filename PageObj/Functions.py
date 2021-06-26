from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://yandex.ru/"

    def find_element(self, locator,timeout=10):
        return WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator,timeout=10):
        return WebDriverWait(self.driver,timeout).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def visible_element(self,locator,timeout=10):
        return WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(locator))

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def filter_urls(self, loop, urls):
        filtredURLS = []
        for url in urls[:5]:
            filtredURLS.append(url.get_attribute('href'))
        filtred = list(filter(lambda x: loop in x, filtredURLS))
        return filtred

    def switch_window(self, handlesNum):
        self.driver.switch_to.window(self.driver.window_handles[handlesNum])

    def current_URL(self):
        return self.driver.current_url

    def prev_pic(self):
        self.driver.find_element_by_css_selector('.MediaViewer-ButtonPrev').click()

    def next_pic(self):
        self.driver.find_element_by_css_selector('.MediaViewer-ButtonNext').click()

    def current_pic(self):
        return self.driver.find_element_by_class_name('MMImage-Origin').get_attribute('src')
