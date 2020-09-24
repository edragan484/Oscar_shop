import time

from DZ_4 import locators, utils


# 1 Item search by name
def test_item_search(browser):
    # Data
    search_text = "The shellcoder's handbook"

    # Arrange
    browser.get(locators.main_page_link)

    # Act
    utils.search_item(browser, search_text)

    # Assert
    item_title = utils.find(browser, locators.item_page_title)
    item_title_text = item_title.text
    assert search_text in item_title_text, \
        "Search page title '%s should contain search text '%s''" % (item_title_text, search_text)

    browser.execute_script("window.scrollBy(0, 500);")
    time.sleep(30)
    item_button = utils.find(browser, locators.button_add_search)
    assert item_button is not None, "Button is on page"
