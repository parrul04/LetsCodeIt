from base.selenium_driver import SeleniumDriver
from utilities.custom_log import CustomLogger
import logging
from time import sleep

class CoursePage(SeleniumDriver):
    log = CustomLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS

    _search_course = 'search-courses'  # id
    _search_button = 'search-course-button'  # id
    _course = "//div[@title='{0}']"
    #_course = "//div[@data-course-id='{0}']"  # xpath
    _enrollButton = 'enroll-button-top'  # id
    _useAnotherCard = "//button[contains(text(), 'Use another card')]"  # xpth
    _card_number = "cardnumber"  # name
    _expDate = 'exp-date'  # name
    _cvc = 'cvc'  # name
    _selectCountry = 'cardCountry'  # id
    # _value = 'US'  # value
    _postalCode = 'zipCode'  # id
    _savecard_checkBox = 'saveCard'  # id
    _confirmEnroll = "//button[@data-test='confirm-enroll']"  # xpath
    _error_message = "//div[@class='dsp-flex-xs m-t-2-xs']//span[contains(text(),'Your card number is invalid.')]" #xpath
    #_home_page = "//a[@class='navbar-brand header-logo']"

    def entercourseName(self, searchCourse):
        self.sendData(searchCourse, self._search_course)

    def clickSearchButton(self):
        self.ElementClick(self._search_button)

    def clickCourse(self, courseName):
        self.ElementClick(self._course.format(courseName), locatorType='xpath')

    def enrollInCourse(self):
        self.ElementClick(self._enrollButton)

    def useAnotherCard(self):
        self.ElementClick(self._useAnotherCard, locatorType='xpath')

    # def enterCCNumber(self, ccNumber):
    #     self.sendData(ccNumber, self._card_number, locatorType='name')

    # def enterExpDate(self, exp):
    #     self.sendData(exp, self._expDate, locatorType='name')
    #
    # def enterCvv(self, cvv):
    #     self.sendData(cvv, self._cvc, locatorType='name')



    def enterCardNumber(self, cardNum):

        # iframe takes atleast 6 sec to show, may take more time

        # sleep(6)
        self.switchIframeByIndex(self._card_number, locatorType='name')
        self.sendData(cardNum, self._card_number, locatorType='name')
        self.defaultContentSwitch()

    def enterExpDate(self, expDate):

        self.switchIframeByIndex(self._expDate, locatorType='name')
        self.sendData(expDate, self._expDate, locatorType='name')
        self.defaultContentSwitch()

    def enterCvc(self, cvc):

        self.switchIframeByIndex(self._cvc, locatorType='name')
        self.sendData(cvc, self._cvc, locatorType='name')
        self.defaultContentSwitch()

    def dropdown(self, text):
        self.DropDown(self._selectCountry, visible_text=text)

    def postalcode(self,postcode):
        self.sendData(postcode, self._postalCode, locatorType='id')

    # def homepage(self):
    #     self.scrollBrowser('up')
    #     self.ElementClick(self._home_page, locatorType='xpath')

    def enterCCdetails(self, ccNumber, exp, cvc, text, postCode):

        self.enterCardNumber(ccNumber) #'123412341234'
        self.enterExpDate(exp)
        self.enterCvc(cvc)

        self.dropdown(text) #'United States of America'
        self.postalcode(postCode)

    def enrollcourse(self,search_course='',courseName='', CCnumber='', exp='', cvc='', country='',  postcode=''):
        self.entercourseName(search_course)
        self.clickSearchButton()
        self.clickCourse(courseName)
        self.enrollInCourse()
        self.scrollBrowser('down')
        self.useAnotherCard()
        self.enterCCdetails(CCnumber, exp, cvc, country, postcode)
        self.scrollBrowser('down')



    def verifyCCDetails(self):
        self.ExplicitWaitType(self.driver, self._error_message, locatorType='xpath')
        errorMessage = self.isElementPresent(self._error_message, locatorType='xpath')
        return errorMessage

    def verifyEnrollfailed(self):

        result = self.isEnabled(self._confirmEnroll, locatorType='xpath', info='Enroll Button')

        return not result






