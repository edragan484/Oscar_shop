from .base_page import BasePage


class MainPage(BasePage):
    main_page_link = "http://selenium1py.pythonanywhere.com"

    search_input_locator = "input#id_q"
    search_submit_locator = "input.btn.btn-default"
    search_title_locator = "div.page-header h1"
    search_result_locator = "article.product_pod"

    def __init__(self, browser):
        BasePage.__init__(self, browser, MainPage.main_page_link)

    def search_item(self, item_text):
        search_input = self.find(MainPage.search_input_locator)
        search_input.clear()

        search_input.send_keys(item_text)
        self.find(MainPage.search_submit_locator).click()

    def get_search_title(self):
        return self.find(MainPage.search_title_locator).text

    def get_search_results(self):
        return self.find_all(MainPage.search_result_locator)






    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
