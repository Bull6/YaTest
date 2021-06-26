from PageObj.Functions import BasePage
from PageObj.Locators import YandexSeacrhLocators




class SearchHelper(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.send_keys(word)
        return search_field

    def click_on_element(self, locator):
        return self.find_element(locator,timeout=2).click()

    def check_visible_element(self,locator):
        return self.visible_element(locator)

