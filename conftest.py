# configuration file for all tests
# can contain frequently used fixtures
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# for each supported browser we have separate function to initialize it's webdriver with language options
# because they're created diffirently
# this method adds scalability because all we have to do is create another function and update supported_browsers dictionary
# no if-s for every browser name is main plus
def launch_chrome_and_add_language_options(user_language: str) -> webdriver:
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    return webdriver.Chrome(options=options)

def launch_firefox_and_add_language_options(user_language: str) -> webdriver:
    options = webdriver.FirefoxOptions()
    options.set_preference("intl.accept_languages", user_language)
    return webdriver.Firefox(options=options)


supported_browsers = {
    'chrome': launch_chrome_and_add_language_options,
    'firefox': launch_firefox_and_add_language_options
}

# now you can specify browser name in command line options by using --browser_name='browser-name'.
# supported variants: chrome, firefox
# and you can specify language in command line option by using --language='language-name'
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', \
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en-us', \
                     help="Choose language in universal format")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    if browser_name in supported_browsers:
        browser = supported_browsers.get(browser_name)(user_language)
        print(f"\nstart {browser_name} browser for test..")
    else:
        joined_browsers = ', '.join(supported_browsers.keys())
        raise pytest.UsageError(f"--browser_name is invalid, supported browsers: {joined_browsers}")

    yield browser
    print("\nquit browser..")
    browser.quit()