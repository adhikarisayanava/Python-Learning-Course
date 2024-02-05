#Fixtures are functions and methods that execute before and after test code blocks execute.
#The setUpModule() and tearDownModule() run before and after all test methods in the module.
#The setUpclass() and tearDownClass() run before and after all test methods in a test class.
#The setUp() and tearDown() run before and after each test method of a test class.

import unittest
from LearningCourse.Unit_Testing.Shapes.square import Square

def setUpModule():
    print('Running setUpModule')


def tearDownModule():
    print('Running tearDownModule')

#@unittest.skip('I am trying to check skip unittest functionality') : This can be used to skip this entire test class
class TestMyModule(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Running setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('Running tearDownClass')

    def setUp(self):
        print('Running setUpMethod')

    def tearDown(self):
        print('Running tearDownMethod')

    def test_case_1(self):
        print('Running test_case_1')
        square = Square(10)
        area = square.area()
        self.assertEqual(area, 100)

    @unittest.skip('I am trying to check skip unittest functionality') #decorator to skip a unittest or a test class
    def test_case_2(self):
        print('Running test_case_2')
        square = Square(11)
        area = square.area()
        self.assertEqual(area,121)