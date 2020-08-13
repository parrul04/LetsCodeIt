"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
import traceback
from selenium import webdriver

class WebDriverFactory():

    def __init__(self, browser):
        """
        Inits WebDriverFactory class

        Returns:
            None
        """
        self.browser = browser
    """
        Set chrome driver and iexplorer environment based on OS

        chromedriver = "C:/.../chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

        PREFERRED: Set the path on the machine where browser will be executed
    """

    def getWebDriverInstance(self):
        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """
        baseUrl = "https://learn.letskodeit.com/"
        if self.browser == "safari":
            # Set safari driver
            driver = webdriver.Safari()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            # Set chrome driver
            #########
            # reCAPTCHA ISSUE WORKOROUND in Chrome webbrowser
            #  https://www.loom.com/share/f2a51d18919d4b70a6d837524ff0e018
            ################
            # first open chrome://version/
            # than copy profilepath from there
            # here in this computer path is
            # /Users/parulagarwal/Library/Application Support/Google/Chrome/Default
            # paste it in opt.argument() and follow the following steps

            opt = webdriver.ChromeOptions()
            opt.add_argument("user-data-dir=/Users/parulagarwal/Library/Application Support/Google/Chrome/Default")
            driver = webdriver.Chrome(options=opt)

        else:
            driver = webdriver.Firefox()
        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(5)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(baseUrl)
        return driver
