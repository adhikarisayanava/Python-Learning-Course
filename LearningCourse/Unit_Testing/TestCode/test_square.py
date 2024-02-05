import unittest
from LearningCourse.Unit_Testing.Shapes.square import Square

class TestSquare(unittest.TestCase):
    def test_area(self):
        square = Square(10)
        area = square.area()
        self.assertEqual(area,100)

    def test_length_with_wrong_type(self):
        with self.assertRaises(TypeError):
            square = Square('10')

    def test_length_with_zero_or_negative(self):
        with self.assertRaises(ValueError):
            square = Square(0)
            square = Square(-1)

#if __name__ == '__main__':
#    unittest.main(verbosity=2)

#Command to run this test : python.exe -m unittest -v
#This command discovers all the test classes whose names start with Test* located in the test_* file and execute the test methods that start with test*. the -m option stands for the module.