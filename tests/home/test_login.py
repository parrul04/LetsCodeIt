# import unittest
# from selenium import webdriver
# from page.home.login_page import LoginPage
# from selenium.webdriver.common.by import By
#
#
# class LoginTests(unittest.TestCase):
#
#     baseUrl = "https://learn.letskodeit.com/"
#     driver = webdriver.Firefox()
#     driver.maximize_window()
#     driver.get(baseUrl)
#     driver.implicitly_wait(10)
#
#     lp = LoginPage(driver)
#     lp.login('test@email.com', 'abcabc')


import unittest
from page.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import pytest
from time import sleep


@pytest.mark.usefixtures("OneTimeSetUP", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self, OneTimeSetUP):
        self.lp = LoginPage(self.driver)
        self.tc = TestStatus(self.driver)


    @pytest.mark.run(order=2)
    def test_ValidLogin(self):

        self.driver.implicitly_wait(5)

        self.lp.login('test@email.com', 'abcabc')

        result1 = self.lp.verifyLoginTitle()
        # assert result1 == True
        self.tc.mark(result1, " Title is not correct")


        result2 = self.lp.verifyLoginSuccessful()
        # assert result2 == True
        self.tc.markFinal("test_ValidLogin", result2, " Element not present here")



    @pytest.mark.run(order=1)
    def test_invalidLogin(self):

        self.driver.implicitly_wait(10)

        # INVALID DATA OPTIONS
        self.lp.logout()
        sleep(3)

        self.lp.login('test.email@com', 'qwe')

        #self.lp.login()
        #self.lp.login(username='test.email@com')
        #self.lp.login(userpassword='abcabc')

        result = self.lp.verifyLiginFailed()
        assert result == True











