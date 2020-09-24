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
    search_title_text = utils.find(browser, locators.search_title).text
    assert search_text in search_title_text, \
        "Search page title '%s should contain search text '%s''" % (search_title_text, search_text)

    search_result = utils.find_all(browser, locators.search_result)
    assert len(search_result) == 1, \
        "Result list should contains only one result, but it contains %s elements" % len(search_result)
    result_item = search_result[0]

    item_image = utils.find(result_item, "img")
    assert item_image is not None, "Image is on page"


