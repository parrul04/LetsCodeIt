from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from base.selenium_driver import SeleniumDriver
import logging
from utilities.custom_log import CustomLogger
from page.home.NavigatonPage import NavigationPage


# Here now all page classes will inherit the selenium class

class LoginPage(SeleniumDriver):


    # so that in log file claaing class will be this Loginpage rather than seleniumDriver class
    log = CustomLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    _loginLink =  "//a[contains(text(),'Login')]"  # Xpath
    _email = 'user_email'
    _password = 'user_password'
    _login_button = 'commit'
    _search_box = 'search-courses'
    _invalid_Login_text =  "//div[contains(text(),'Invalid email or password.')]"
    _usersettingIcon = "//img[@alt='test@email.com']"
    _logout = "//a[contains(text(), 'Log Out')]"

    def clickLoginLink(self):
        self.ElementClick(self._loginLink, locatorType='xpath')

    def enterEmail(self, email):
        self.sendData(email, self._email, locatorType='id')

    def enterPassword(self, password):
        self.sendData(password, self._password, locatorType='id')

    def clickLoginButton(self):
        self.ElementClick(self._login_button, locatorType='name')

    # def clickuserSettingIcon(self):
    #     self.ElementClick(self._usersettingIcon, locatorType='xpath')

    def clickLogout(self):
        self.ElementClick(self._logout, locatorType='xpath')

    def logout(self):
        #self.clickuserSettingIcon()
        self.nav.click_UserIcon()
        self.clickLogout()

    def login(self, username='', userpassword=''):

        self.clickLoginLink()
        self.enterEmail(username)
        self.enterPassword(userpassword)
        self.clickLoginButton()

    # def getloginLink(self):
    #     return  self.driver.find_element(By.PARTIAL_LINK_TEXT, self._loginLink)
    #
    # def getEmail(self):
    #     return self.driver.find_element(By.ID, self._email)
    #
    # def getPassword(self):
    #     return  self.driver.find_element(By.ID, self._password)
    #
    # def getLoginButton(self):
    #     return self.driver.find_element(By.NAME, self._login_button)

    # def clickLoginLink(self):
    #     self.getloginLink().click()
    #
    # def enterEmail(self, email):
    #     self.getEmail().send_keys(email)
    #
    # def enterPassword(self, password):
    #     self.getPassword().send_keys(password)
    #
    # def clickLoginButton(self):
    #     self.getLoginButton().click()
    #
    #
    # def login(self, username, userpassword):
    #
    #     self.clickLoginLink()
    #     self.enterEmail(username)
    #     self.enterPassword(userpassword)
    #     self.getLoginButton()
    #
    #

    def verifyLoginSuccessful(self):
        result = self.isElementPresent(self._search_box, locatorType='id')
        return result


    def verifyLiginFailed(self):
        result = self.isElementPresent(self._invalid_Login_text, locatorType='xpath')
        return result

    def verifyLoginTitle(self):
        #Let's Kode It   #Google
        if "Let's Kode It" in self.get_title():
            return True
        else:
            return False


