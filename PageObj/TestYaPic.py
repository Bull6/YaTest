from PageObj.YandexPages import SearchHelper
from PageObj.Locators import YandexImageLocators


#Picture Tests

def test_PicIcon(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    pic_link = yandex_main_page.find_element(YandexImageLocators.LOCATOR_YANDEX_LIST_ITEM_IMAGE)
    pic_link.click()
    yandex_main_page.switch_window(1)

    url = yandex_main_page.current_URL()
    assert "https://yandex.ru/images/" in url

def test_Top1Pic(browser):
    yandex_main_page = SearchHelper(browser)

    pic_link = yandex_main_page.find_element(YandexImageLocators.LOCATOR_YANDEX_FIRST_IMAGE)
    pic_link_text = pic_link.text
    pic_link.click()

    current_text = yandex_main_page.find_element(YandexImageLocators.LOCATOR_YANDEX_SEARCH_FIELD_IMAGE).text
    assert pic_link_text == current_text

def test_OpenPic(browser):
    yandex_main_page = SearchHelper(browser)

    pic_link = yandex_main_page.find_element(YandexImageLocators.LOCATOR_YANDEX_OPEN_IMAGE)
    pic_link.click()

    element = yandex_main_page.check_visible_element(YandexImageLocators.LOCATOR_YANDEX_VIEW_IMAGE)
    assert element

def test_NextPic(browser):
    yandex_main_page = SearchHelper(browser)

    global pic1
    pic1 = yandex_main_page.current_pic()
    yandex_main_page.next_pic()
    pic2 = yandex_main_page.current_pic()

    assert pic1 != pic2

def test_PrevPic(browser):
    yandex_main_page = SearchHelper(browser)

    yandex_main_page.prev_pic()
    pic = yandex_main_page.current_pic()

    assert pic1 == pic