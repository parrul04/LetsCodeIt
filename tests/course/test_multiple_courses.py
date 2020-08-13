import unittest
from page.courses.course_page import CoursePage
from page.home.NavigatonPage import NavigationPage
from utilities.teststatus import TestStatus
import pytest
from ddt import ddt, data, unpack
from utilities.readData import getCsvData


@pytest.mark.usefixtures("OneTimeSetUP", "setUp")
@ddt
class CourseTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, OneTimeSetUP):
        self.cp = CoursePage(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    @pytest.mark.run(order=1)
    #@data(('javascript', 'JavaScript for beginners' ,'1234123412341234', '09/23', '345', 'United States of America', '1234'),
          #('python', 'Learn Python 3 from scratch' ,'1234123412341234', '09/25', '333', 'United States of America', '1234'))
    @data(*getCsvData("/Users/parulagarwal/Documents/workspace_python/LetsCodeIt/dataFile.csv"))
    @unpack
    def test_InvalidCourseEnroll(self, searchCourse, course_name , ccNum, ccexp, ccCVC, country, postalcode):


        self.cp.enrollcourse(searchCourse, course_name, ccNum, ccexp, ccCVC, country, postalcode )

        result = self.cp.verifyCCDetails()

        self.ts.markFinal('test_CourseEnroll', result, 'Error message not exist')

        # result = self.cp.verifyEnrollfailed()
        #
        # self.ts.markFinal('test_InvalidCourseEnroll', result, 'Error message not exist')
        #self.cp.homepage()
        self.nav.click_home()



