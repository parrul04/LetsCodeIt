from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
import logging
import utilities.custom_log as cl
from utilities.custom_log import CustomLogger
import time
import os
from selenium.webdriver.support.select import Select


class SeleniumDriver():


    #log = cl.CustomLogger(logging.DEBUG)
    log = CustomLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    # **************************** GET BYTYPE ****************************

    def getByType(self, locatorType):

        locatorType = locatorType.lower()

        if locatorType == "id":
            return  By.ID

        elif locatorType == 'xpath':
            return By.XPATH

        elif locatorType == "name":
            return By.NAME

        elif locatorType == 'link':
            return By.LINK_TEXT

        elif locatorType == 'partiallink':
            return By.PARTIAL_LINK_TEXT

        elif locatorType =='tag':
            return By.TAG_NAME

        elif locatorType == 'class':
            return By.CLASS_NAME

        elif locatorType == 'cssselector':
            return By.CSS_SELECTOR

        else:
            print(" Locator Type not correct")
        return False

    # ****************************  GET ELEMENT  ****************************

    def getElement(self, locator, locatorType='id'):

        element = None

        try:

            byType = self.getByType(locatorType)

            element = self.driver.find_element(byType, locator)
            self.log.info("  Element found by locator: " + locator + ' and locator Type: ' + locatorType)

        except:
            self.log.info("  Element not found  by locator: " + locator + ' and locator Type: ' + locatorType)

        return element

    # ************* GET ELEMENT LIST  **************

    def getElementList(self, locator, locatorType='id'):

        elementList = None

        try:

            byType = self.getByType(locatorType)

            elementList = self.driver.find_elements(byType, locator)
            self.log.info("  ElementList found by locator: " + locator + ' and locator Type: ' + locatorType)

        except:
            self.log.info("  ElementList not found  by locator: " + locator + ' and locator Type: ' + locatorType)

        return elementList


    # **************************** ELEMENT CLICK ****************************

    def ElementClick(self, locator='', locatorType='id', element=None):

        # element=None means if element is  given then directly click on element otherwise find element first using locator

        try:
            if locator:
                element = self.getElement(locator, locatorType)

            element.click()
            self.log.info("  Element clicked by locator: " + locator + ' and locator Type: ' + locatorType)

        except:
            self.log.error("  EXCEPTION occured :: Element cannot clicked by locator: " +
                           locator + ' and locator Type: ' + locatorType)
            print_stack()

    # **************************** SEND DATA  ****************************

    def sendData(self, data, locator='', locatorType='id', element=None):

        try:
            if locator:
                element = self.getElement(locator, locatorType)
            # Always clear data from data fielf first
            element.clear()
            element.send_keys(data)
            self.log.info("  Data send by locator: " + locator + ' and locator Type: ' + locatorType)

        except:
            self.log.error("  EXCEPTION occored :: Data not send  clicked by locator: "
                           + locator + ' and locator Type: ' + locatorType)
            print_stack()

    def get_title(self):
        return self.driver.title

# **************************** ELEMENT PRESENT  ****************************

    def isElementPresent(self, locator='', locatorType='id', element=None):

        try:
            if locator:
                element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("  Element present  by locator: " + locator
                              + ' and locator Type: ' + locatorType)
                return True
            else:
                self.log.error("  Element not present  by locator: "
                               + locator + ' and locator Type: ' + locatorType)
                return False

        except:
            self.log.error( "  EXCEPTION occured :: "+ " Element not present  by locator: "
                               + locator + ' and locator Type: ' + locatorType)
            return False

    def isElementsPresent(self, locator='', locatorType='id',element_list=None):

        try:
            if locator:
                locatorType = locatorType.lower()
                byType = self.getByType(locatorType)
                element_list = self.driver.find_elements(byType, locator)

            if element_list>0:
                self.log.info("   Elements present  by locator: " + locator + ' and locator Type: ' + locatorType)
                return True
            else:
                self.log.info("   Elements not present by locator: " + locator + ' and locator Type: ' + locatorType)
                return False

        except:
            self.log.error("  EXCEPTION occured "+ " Elements not present  by locator: " + locator + ' and locator Type: ' + locatorType)
            return False

 # **************************** SCREENSHOTS  ****************************

    def screenShots(self, resultMessage):

        """
        TAKE SCREENSHOTS of current open webpage
        """
        FileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"

        # now goto screenshoot dir for that go out from current base dir so use ..

        screenshotdir = "../screenshots/"

         # now the file path
        RelativeFilepath =  screenshotdir + FileName

        # current dir

        currentdir = os.path.dirname(__file__)

        # Destinationdir relative to current dir

        destinationfilePath = os.path.join( currentdir , RelativeFilepath)

        destinationdirpath = os.path.join( currentdir, screenshotdir )

        try:
            if not os.path.exists(destinationdirpath):
                os.makedirs(destinationdirpath)
            self.driver.save_screenshot(destinationfilePath)
            self.log.info(" ##Screenshot Saved to directory " + destinationdirpath)

        except:
            self.log.error("### EXCEPTION OCCOURED!!!")
            print_stack()

# **************************** EXPLICIT WAIT  ****************************

    def ExplicitWaitType(self, driver, locator='', locatorType='id', timeout=10, poll_frequency=1):

        element = None

        try:
            byType = self.getByType(locatorType)
            self.log.info("  Wait for max " + str(timeout) + " before element to be clickable")

            wait = WebDriverWait(self.driver, timeout, poll_frequency,
                                 ignored_exceptions=(NoSuchElementException,
                                                     ElementNotSelectableException,
                                                     ElementNotVisibleException))
            element = wait.until(EC.element_to_be_clickable((byType, locator)))

            self.log.info("  Element appeared on webpage  by locator: " + locator + ' and locator Type: ' + locatorType)

        except:
            self.log.error("  EXCEPTION occured "+" Element not appeared on webpage  by locator: " + locator + ' and locator Type: ' + locatorType)
            print_stack()

        return element

    #### ******* NEW METHODS *********

###   ********* SCROLL BROWSER UP AND DOWN   *************

    def scrollBrowser(self, direction='up'):

        # it will scroll the browser up and down

        if direction == 'up':
            self.driver.execute_script("window.scrollBy(0, -1000);")

        if direction == 'down':
            self.driver.execute_script("window.scrollBy(0, 1000);")

### **********************    ELEMENT DISPLAYED    *****************

    def isElementDispalyed(self, locator, locatorType, element=None):

        isDisplayed = False

        try:
            if locator:
                element = self.getElement(locator, locatorType)
            if element:
                isDispalyed = element.is_displayed()  # return either True or False
                self.log.info("  Element diaplayed by locator :: " + locator
                              + " and locatorType :: " + locatorType)
            else:
                self.log.info("  Element not diaplayed by locator :: " + locator
                              + " and locatorType :: " + locatorType)
            return isDisplayed


        except:
            self.log.error(" Exception occured :: Element not diaplayed by locator :: " + locator
                          + " and locatorType :: " + locatorType)
            return False


#### ********* GetText  *************

    def getText(self, locator='', locatorType='id', element=None):

        try:
            if locator:
                self.log.debug(" In Locator Condition")
                element = self.getElement(locator, locatorType)
            self.log.debug(" Before finding text")
            text = element.text
            self.log.debug(" After finding element the size is :: " + str(len(text)))

            if len(text) == 0:
                text = element.get_attribute("innerText")
                self.log.info("Getting text on element:")
                self.log.info(" The text is :: ' " + text + "'")
                text = text.strip()

        except:
            self.log.error(" Failed to get the text on element")
            print_stack()
            text= None
        return text


    #### ***********  Dropdown Element (Select class) ********
    def DropDown(self, locator='', locatorType='id', index='',value='', visible_text='', element=None):

        try:
            if locator:
                element = self.getElement(locator, locatorType)
            sel = Select(element)

            if index:
                sel.select_by_index(index)
                self.log.info(" Element seleced by index:: " + str(index) )

            if value:
                sel.select_by_value(value)
                self.log.info(" Element seleced by value:: " + str(value) )

            if visible_text:
                sel.select_by_visible_text(visible_text)
                self.log.info(" Element seleced by visible text:: " + str(visible_text) )

        except:
            self.log.error(" Exception occured element not selected from dropdown")
            print_stack()

    ####### ************* IFRAME SWITCH ***************

    def iframeSwitch(self, id='', name='', index=None):

        if id:
            self.driver.switch_to.frame(id)

        elif name:
            self.driver.switch_to.frame(name)

        else:
            self.driver.switch_to.frame(index)

    def defaultContentSwitch(self):

        self.driver.switch_to.default_content()


    # Iframe workaround

    def switchIframeByIndex(self, locator='', locatorType='id'):

        """
        Get iframe index using element locator inside iframe

        Parameters ::

        1). Reqiured:
                    locator
        2) optional
                    LocatorType

        Return :
                Index of ifrrame

        Exception :
                None


        """

        result = False

        try:

            iframe_list = self.getElementList("//iframe", 'xpath')
            self.log.info("   Length of iframe List : " + str(len(iframe_list)))

            for i in range(len(iframe_list)):
                self.iframeSwitch(index=iframe_list[i])
                result = self.isElementPresent(locator, locatorType)

                if result:
                    # as soon as we find our element inside the frame we will break the loop
                    # But we are stil inside that iframe
                    self.log.info("  Iframe index is :")
                    self.log.info(str(i))
                    break
                self.defaultContentSwitch()

            return result

        except:
            self.log.error("  Iframe not found")
            return result



#  ****************  GetElementAttributeValue   ***********

    # def getElementAttributeValue(self, attribute, element=None, locator="", locatorType="id"):
    #     """
    #     Get value of the attribute of element
    #
    #     Parameters:
    #         1. Required:
    #             1. attribute - attribute whose value to find
    #
    #         2. Optional:
    #             1. element   - Element whose attribute need to find
    #             2. locator   - Locator of the element
    #             3. locatorType - Locator Type to find the element
    #
    #     Returns:
    #         Value of the attribute
    #     Exception:
    #         None
    #     """
    #     if locator:
    #         element = self.getElement(locator=locator, locatorType=locatorType)
    #     value = element.get_attribute(attribute)
    #     return value
    #
    # ###### ******** IsEnable **************
    #
    # def isEnabled(self, locator, locatorType="id", info=""):
    #     """
    #     Check if element is enabled
    #
    #     Parameters:
    #         1. Required:
    #             1. locator - Locator of the element to check
    #         2. Optional:
    #             1. locatorType - Type of the locator(id(default), xpath, css, className, linkText)
    #             2. info - Information about the element, label/name of the element
    #     Returns:
    #         boolean
    #     Exception:
    #         None
    #     """
    #     element = self.getElement(locator, locatorType=locatorType)
    #     enabled = False
    #     try:
    #         attributeValue = element.get_attribute("disabled")
    #         self.log.info(" ATTRIBUTEVALUE FOR BUTTON IS: " + str(attributeValue))
    #         #attributeValue = self.getElementAttributeValue(element=element, attribute="disabled")
    #         if attributeValue is not None:
    #             enabled = element.is_enabled()
    #             self.log.info("Enabled value is: " + str(enabled))
    #         else:
    #             value = element.get_attribute("class")
    #             #value = self.getElementAttributeValue(element=element, attribute="class")
    #             self.log.info("Attribute value From Application Web UI --> :: " + value)
    #             enabled = not ("disabled" in value)
    #         if enabled:
    #             self.log.info("Element :: '" + info + "' is enabled")
    #         else:
    #             self.log.info("Element :: '" + info + "' is not enabled")
    #     except:
    #         self.log.error("Element :: '" + info + "' state could not be found")
    #     return enabled

    def getElementAttributeValue(self, attribute, element=None, locator="", locatorType="id"):
        """
        Get value of the attribute of element

        Parameters:
            1. Required:
                1. attribute - attribute whose value to find

            2. Optional:
                1. element   - Element whose attribute need to find
                2. locator   - Locator of the element
                3. locatorType - Locator Type to find the element

        Returns:
            Value of the attribute
        Exception:
            None
        """
        if locator:
            element = self.getElement(locator=locator, locatorType=locatorType)
        value = element.get_attribute(attribute)
        return value

    def isEnabled(self, locator, locatorType="id", info=""):
        """
        Check if element is enabled

        Parameters:
            1. Required:
                1. locator - Locator of the element to check
            2. Optional:
                1. locatorType - Type of the locator(id(default), xpath, css, className, linkText)
                2. info - Information about the element, label/name of the element
        Returns:
            boolean
        Exception:
            None
        """
        element = self.getElement(locator, locatorType=locatorType)
        enabled = False
        try:
            attributeValue = self.getElementAttributeValue(element=element, attribute="disabled")
            if attributeValue is not None:
                enabled = element.is_enabled()
            else:
                value = self.getElementAttributeValue(element=element, attribute="class")
                self.log.info("Attribute value From Application Web UI --> :: " + value)
                enabled = not ("disabled" in value)
            if enabled:
                self.log.info("Element :: '" + info + "' is enabled")
            else:
                self.log.info("Element :: '" + info + "' is not enabled")
        except:
            self.log.error("Element :: '" + info + "' state could not be found")
        return enabled

























