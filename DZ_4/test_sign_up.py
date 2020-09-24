import random

from DZ_4 import locators, utils


def test_sign_up(browser):
    # Data
    mail = ''
    email = ''
    for x in range(1):
        mail = mail + random.choice(list('1234567890qwertyuiop')) + random.choice(list('qwertyuiop1234567890ASDFGHJKLZXCVBBNNMM'))
        email = mail + '@' + 'gmail.com'
        print(email)

    # Arrange
    browser.get(locators.main_page_link)

    # Act
    button_registration = utils.find(browser, locators.login_link)
    button_registration.click()

    reg_email = utils.find(browser, locators.email_sign_up)
    reg_email.send_keys(email)

    reg_password_new = utils.find(browser, locators.password_sign_up)
    reg_password_new.send_keys("Coronavirus2020")

    reg_password_new = utils.find(browser, locators.submit_pass_sign_up)
    reg_password_new.send_keys("Coronavirus2020")

    button_submit_reg = utils.find(browser, locators.submit_sign_up_button)
    button_submit_reg.click()

    # Assert
    welcome_text_pos = utils.find(browser, locators.welcome_text_sign_up)
    welcome_text = welcome_text_pos.text
    assert "Thanks for registering!" == welcome_text, \
        "'%s' Registration successful" % welcome_text
