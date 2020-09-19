from selenium import webdriver
import random
from Oscar_shop import locators as _locators


def find(parent, locator): return parent.find_element_by_css_selector(locator)


def find_all(parent, locator): return parent.find_elements_by_css_selector(locator)


def find_xpath(parent, locator): return parent.find_element_by_xpath(locator)


def find_link(parent, locator): return parent.find_element_by_link_text(locator)


# 1 Item search by name
def search_item():
    # Data
    search_text = "The shellcoder's handbook"

    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(_locators.main_page_link)

        search_input = find(_locators.search_input)
        search_input.clear()

        # Act
        search_input.send_keys(search_text)
        find(browser, _locators.search_submit).click()

        # Assert
        search_title_text = find(browser, _locators.search_title).text
        assert search_text in search_title_text, \
            "Search page title '%s should contain search text '%s''" % len(search_title_text, search_text)

        search_result = find_all(browser, _locators.search_result)
        assert len(search_result) == 1, \
            "Result list should contains only one result, but it contains %s elements" % len(search_result)
        result_item = search_result[0]

        item_image = find(result_item, "img")
        assert search_text in item_image.get_attribute("alt"), \
            "Item should contain image with correct alt, but it doesn't"

        item_desc = find(result_item, "h3 a")
        assert search_text in item_desc.text, "Search result should contain searching string in its text"

    finally:
        # print("Done")
        browser.quit()


# 2 Registration
def sign_up():
    # Data
    mail = ''
    email = ''
    for x in range(1):
        mail = mail + random.choice(list('qwertyuiop')) + random.choice(list('1234567890ASDFGHJKLZXCVBBNNMM'))
        email = mail + '@' + 'gmail.com'
        print(email)
    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.get(_locators.main_page_link)

        # Act
        button_registration = find(browser, _locators.login_link)
        button_registration.click()

        reg_email = find(browser, _locators.email_sign_up)
        reg_email.send_keys(email)

        reg_password_new = find(browser, _locators.password_sign_up)
        reg_password_new.send_keys("Coronavirus2020")

        reg_password_new = find(browser, _locators.submit_pass_sign_up)
        reg_password_new.send_keys("Coronavirus2020")

        button_submit_reg = find(browser, _locators.submit_sign_up_button)
        button_submit_reg.click()

        # Assert
        welcome_text_pos = find(browser, _locators.welcome_text_sign_up)
        welcome_text = welcome_text_pos.text
        assert "Thanks for registering!" == welcome_text, \
            "'%s' Registration successful" % welcome_text

    finally:
        browser.quit()
        print("Done!")


# 3 Authorization
def sign_in():
    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(_locators.main_page_link)

        # Act
        button_enter = find(browser, _locators.login_link)
        button_enter.click()

        auth_email = find(browser, _locators.email_sign_in)
        auth_email.send_keys("reg1@gmail.com")

        auth_password = find(browser, _locators.password_sign_in)
        auth_password.send_keys("Coronavirus2020")

        button_submit = find(browser, _locators.submit_sign_in_button)
        button_submit.click()

        # Assert
        welcome_text_pos = find(browser, _locators.welcome_text_sign_in)
        # welcome_text = welcome_text_pos.text
        assert "Welcome back" == welcome_text_pos.text, \
            "Successful authorization '%s'" % (welcome_text_pos.text)

    finally:
        print("Done")
        browser.quit()


# 4 Change_language
def change_language():
    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(_locators.main_page_link)

        # Act
        browser.find_element_by_tag_name("select").click()
        browser.find_element_by_css_selector("[value='it']").click()

        button_language_go = find(browser, _locators.button_language_go)
        button_language_go.click()

        # Assert
        product_menu_italiano = find(browser, _locators.menu_products)
        assert "Naviga nel negozio" == product_menu_italiano.text, \
            "Products menu should contain italian text '%s''" % (product_menu_italiano.text)

        basket_italiano = find(browser, _locators.button_basket)
        assert "Visualizza carrello" == basket_italiano.text, \
            "Basket button should contain italian name '%s''" % (basket_italiano.text)

    finally:
        print("Done")
        browser.quit()


# 5 Add_item
def add_item():
    # Data
    locator_item = "The shellcoder's handbook"

    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(_locators.main_page_link)
        # sign_up()
        # Act
        all_products = find_xpath(browser, _locators.all_products)
        all_products.click()

        item = find_link(browser, locator_item)
        item.click()

        button_add = find(browser, _locators.button_add)
        button_add.click()

        # Assert
        add_note = find(browser, _locators.add_item_notification)
        assert locator_item in add_note.text, \
            "'%s' has been added to your basket." % locator_item

        button_basket = find(browser, _locators.button_basket)
        button_basket.click()

        item_in_basket = find(browser, _locators.item_in_basket)
        assert locator_item in item_in_basket.text, "'%s' in '%s'" % (locator_item, item_in_basket)

    finally:
        print("Done")
        browser.quit()


def remove_item():
    add_item()
    # Data

    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(_locators.main_page_link)

        button_basket = find(browser, _locators.button_basket)
        button_basket.click()

        # Act
        item_quantity = find(browser, _locators.item_quantity)
        item_quantity.clear()
        item_quantity.send_keys('0')

        button_update = find(browser, _locators.button_update_quantity)
        button_update.click()

        # Assert
        basket_note = find(browser, _locators.basket_note_change)
        assert "Your basket is now empty" == basket_note.text, "Basket is empty after removing"

    finally:
        browser.quit()
        print("Done!")


def offers():
    # Data

    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(_locators.main_page_link)

        # Act
        offers_push = find(browser, _locators.offers_button)
        offers_push.click()

        # Assert
        page_offer = find(browser, _locators.page_title)
        assert page_offer.text == "Offers", "'%s' in page name" % page_offer.text

    finally:
        browser.quit()
        print("Done!")


#search_item()
#sign_up()
#sign_in()
#change_language()
#add_item()
#remove_item()
#offers()

