from PageObj.BaseApp import BasePage
from PageObj.Locators import YandexSeacrhLocators
from PageObj.Locators import YandexImageLocators



class SearchHelper(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        #search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_element(self, locator):
        return self.find_element(locator,timeout=2).click()

    def check_navigation_bar(self):
        all_list = self.find_elements(YandexSeacrhLocators.LOCATOR_YANDEX_NAVIGATION_BAR,timeout=2)
        nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_menu

    def check_visible_element(self,locator):
        return self.visible_element(locator)

