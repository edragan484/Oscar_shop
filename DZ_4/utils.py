from DZ_4 import locators


def find(parent, locator): return parent.find_element_by_css_selector(locator)


def find_all(parent, locator): return parent.find_elements_by_css_selector(locator)


def find_xpath(parent, locator): return parent.find_element_by_xpath(locator)


def find_link(parent, locator): return parent.find_element_by_link_text(locator)


# Search item on main page
def search_item(browser, text):
    search_input = find(browser, locators.search_input)
    search_input.clear()

    search_input.send_keys(text)
    find(browser, locators.search_submit).click()
