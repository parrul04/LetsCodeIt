from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from base.selenium_driver import SeleniumDriver
import logging
from utilities.custom_log import CustomLogger


# Here now all page classes will inherit the selenium class

class NavigationPage(SeleniumDriver):


    # so that in log file claaing class will be this Loginpage rather than seleniumDriver class
    log = CustomLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _home_page = "//a[@class='navbar-brand header-logo']"
    _my_course = "//a[contains(text(),'My Courses')]"
    _All_course = "//a[contains(text(),'All Courses')]"
    _Practice = "//a[contains(text(),'Practice')]"
    _user_setting_icon = "//a[@class='fedora-navbar-link navbar-link dropdown-toggle open-my-profile-dropdown']"

    def click_home(self):
        self.scrollBrowser('up')
        self.ElementClick(self._home_page, locatorType='xpath')

    def click_My_Course(self):
        self.scrollBrowser('up')
        self.ElementClick(self._my_course, locatorType='xpath')

    def click_All_course(self):
        self.scrollBrowser('up')
        self.ElementClick(self._All_course, locatorType='xpath')

    def click_UserIcon(self):
        self.scrollBrowser('up')
        self.ElementClick(self._user_setting_icon, locatorType='xpath')


