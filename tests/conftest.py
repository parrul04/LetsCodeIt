# import pytest
#
# @pytest.fixture()
# def setUp():
#     print(" Running method level SetUp")
#     yield
#     print(" Running method level TearDown")
#
#
# @pytest.fixture(scope="class")
# def OneTimeSetUP(request, browser):
#     print(" Running class level SetUp")
#     if browser == 'firefox':
#         value = 10
#         print("Running test on Firefox")
#     else:
#         value = 20
#         print("Running test on Chrome")
#
#     # means if the class attribute we re getting request from is not None
#     if request.cls is not None:
#         # then this value will be avilable to complete class instance
#         request.cls.value = value
#
#
#     # this will return value to the place where this OneTimeSetUp fixture is used
#     yield value
#     print(" Running class level Teardown")
#
#
# # parser method pytest_addoption is an internal pytest implementation
# def pytest_addoption(parser):
#     parser.addoption("--browser")
#     parser.addoption("--OSType", help="Type os type")
#
# # nOw create a fixture to use
# @pytest.fixture(scope='session')
# def browser(request):
#     return request.config.getoption("--browser")
#
# @pytest.fixture(scope='session')
# def osType(request):
#     return request.config.getoption("--osType")


import pytest
from selenium import webdriver
from base.webdriverfactory import WebDriverFactory
from page.home.login_page import LoginPage

@pytest.fixture()
def setUp():
    print(" Running method level SetUp")
    yield
    print(" Running method level TearDown")


@pytest.fixture(scope="class")
def OneTimeSetUP(request, browser):
    print(" Running class level SetUp")
    # if browser == 'chrome':
    #     #########
    #     # reCAPTCHA ISSUE WORKOROUND in Chrome webbrowser
    #     #  https://www.loom.com/share/f2a51d18919d4b70a6d837524ff0e018
    #     ################
    #     # first open chrome://version/
    #     # than copy profilepath from there
    #     # here in this computer path is
    #     # /Users/parulagarwal/Library/Application Support/Google/Chrome/Default
    #     # paste it in opt.argument() and follow the following steps
    #
    #     opt = webdriver.ChromeOptions()
    #     opt.add_argument("user-data-dir=/Users/parulagarwal/Library/Application Support/Google/Chrome/Default")
    #     baseUrl = "https://learn.letskodeit.com/"
    #     driver = webdriver.Chrome(options=opt)
    #     driver.get(baseUrl)
    #     driver.maximize_window()
    #     driver.implicitly_wait(10)
    #     print("Running test on Chrome")
    # else:
    #     baseUrl = "https://learn.letskodeit.com/"
    #     driver = webdriver.Firefox()
    #     driver.get(baseUrl)
    #     driver.maximize_window()
    #     driver.implicitly_wait(10)
    #     print("Running test on Firefox")

    wd = WebDriverFactory(browser)
    driver = wd.getWebDriverInstance()

    # create login_page instance here and login to application

    lp = LoginPage(driver)
    lp.login('test@email.com', 'abcabc')

    # means if the class attribute we re getting request from is not None
    if request.cls is not None:
        # then this value will be avilable to complete class instance
        request.cls.driver = driver


    # this will return value to the place where this OneTimeSetUp fixture is used
    yield driver
    driver.quit()
    print(" Running class level Teardown")


# parser method pytest_addoption is an internal pytest implementation
def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--OSType", help="Type os type")

# nOw create a fixture to use
@pytest.fixture(scope='session')
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope='session')
def osType(request):
    return request.config.getoption("--osType")


