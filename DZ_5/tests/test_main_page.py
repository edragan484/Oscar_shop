from DZ_5.pages.main_page import MainPage


class TestMainPage:
    # 1 Item search by name
    def test_item_search(self, browser):
        # Data
        search_text = "The shellcoder's handbook"

        # Arrange
        main_page = MainPage(browser)
        main_page.open()

        # Act
        main_page.search_item(search_text)

        # Assert
        search_title_text = main_page.get_search_title()
        assert search_text in search_title_text, \
            "Search page title '%s should contain search text '%s''" % (search_title_text, search_text)

        search_result = main_page.get_search_results()
        assert len(search_result) == 1, \
            "Result list should contains only one result, but it contains %s elements" % len(search_result)
        result_item = search_result[0]

        item_image = MainPage.find_in_element(result_item, "img")
        assert item_image is not None, "Image is on page"

        assert search_text in item_image.get_attribute("alt"), \
            "Item should contain image with correct alt, but it doesn't"

        item_desc = MainPage.find_in_element(result_item, "h3 a")
        assert search_text in item_desc.text, "Search result should contain searching string in its text"
