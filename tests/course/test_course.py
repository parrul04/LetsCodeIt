import unittest
from page.courses.course_page import CoursePage
from utilities.teststatus import TestStatus
import pytest


@pytest.mark.usefixtures("OneTimeSetUP", "setUp")
class CourseTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, OneTimeSetUP):
        self.cp = CoursePage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_InvalidCourseEnroll(self):


        self.cp.enrollcourse('javascript', 'JavaScript for beginners' ,'1234123412341234', '09/23', '345', 'United States of America', '1234')

        result = self.cp.verifyCCDetails()

        self.ts.markFinal('test_CourseEnroll', result, 'Error message not exist')

        # result = self.cp.verifyEnrollfailed()
        #
        # self.ts.markFinal('test_InvalidCourseEnroll', result, 'Error message not exist')

        #




