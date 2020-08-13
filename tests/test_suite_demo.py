import unittest
from tests.home.test_login import LoginTests
from tests.course.test_multiple_courses import CourseTest


# get all test from test classes

tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(CourseTest)


# create test suite

smoke_test = unittest.TestSuite([tc1, tc2])

# run testsuite

unittest.TextTestRunner(verbosity=2).run(smoke_test)
