from PageObj.YandexPages import SearchHelper
from PageObj.Locators import YandexSeacrhLocators
from PageObj.Locators import YandexImageLocators



def test_Search_Field(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    element = yandex_main_page.check_visible_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_FIELD)
    assert element


def test_Suggest(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.enter_word("Тензор")
    element = yandex_main_page.check_visible_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_SUGGEST)
    assert element

def test_TableSearch(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.enter_word("\n")
    element = yandex_main_page.check_visible_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_TABLE)
    assert element

def test_Top5Tensor(browser):
    yandex_main_page = SearchHelper(browser)
    urls = yandex_main_page.find_elements(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_TENSOR)
    res = yandex_main_page.filter_urls('tensor.ru', urls)
    assert len(res) > 5
