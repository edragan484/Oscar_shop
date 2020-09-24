import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                    help="Choose GUI language for tests")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    if language is None: raise pytest.UsageError("test run should contain language for test")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})

    print("\nopen browser for test..")

    document = webdriver.Chrome(options=options)
    document.implicitly_wait(5)

    yield document

    print("\nquit browser..")
    document.quit()
