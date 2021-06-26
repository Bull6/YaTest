from selenium.webdriver.common.by import By

class YandexSeacrhLocators:
    #For_test_Textbox
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")

    #For_test_Suggest
    LOCATOR_YANDEX_SEARCH_SUGGEST = (By.CSS_SELECTOR, ".mini-suggest__popup.mini-suggest__popup_theme_flat.mini-suggest__popup_visible")

    #For_test_TableSearch
    LOCATOR_YANDEX_SEARCH_TABLE = (By.CSS_SELECTOR, ".content__left")

    #For_test_Top5Tensor
    LOCATOR_YANDEX_SEARCH_TENSOR = (By.CSS_SELECTOR, ".OrganicTitle-Link")

class YandexImageLocators:
    #For_test_PicIcon
    LOCATOR_YANDEX_LIST_ITEM_IMAGE = (By.LINK_TEXT, "Картинки")

    #For_test_Top1Pics
    LOCATOR_YANDEX_FIRST_IMAGE = (By.CSS_SELECTOR, ".PopularRequestList-Shadow")
    LOCATOR_YANDEX_SEARCH_FIELD_IMAGE = (By.CLASS_NAME, "input__control")

    #For_test_OpenPic
    LOCATOR_YANDEX_OPEN_IMAGE = (By.CSS_SELECTOR, ".serp-item__preview")
    LOCATOR_YANDEX_VIEW_IMAGE = (By.CSS_SELECTOR, ".MMImageWrapper")

    #For_test_Next/PrevPic
    LOCATOR_YANDEX_CURRENT_IMAGE = (By.CLASS_NAME, "MMImage-Origin")
    LOCATOR_YANDEX_PREV_BUTTON_IMAGE = (By.CSS_SELECTOR, ".MediaViewer-ButtonPrev")
    LOCATOR_YANDEX_NEXT_BUTTON_IMAGE = (By.CSS_SELECTOR, ".MediaViewer-ButtonNext")
