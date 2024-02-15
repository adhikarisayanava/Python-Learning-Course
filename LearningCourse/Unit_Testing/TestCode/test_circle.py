import unittest
import math
from LearningCourse.Unit_Testing.Shapes.circle import Circle
from LearningCourse.Unit_Testing.Shapes.shape import Shape

class TestCircle(unittest.TestCase):
    def test_circle_instance_of_shape(self):
        circle = Circle(10)
        self.assertIsInstance(circle, Shape)

    def test_circle_negative_radius(self):
        with self.assertRaises(ValueError):
            circle = Circle(-1)

    def test_area(self):
        circle = Circle(2.5)
        self.assertEqual(circle.area(), math.pi * 2.5 * 2.5)

    def test_dummy(self):
        self.assertAlmostEqual(4.4555, 4.4556, msg="first and second are not almost equal", delta=0.0001)
