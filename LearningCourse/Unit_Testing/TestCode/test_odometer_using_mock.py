from unittest import TestCase
from unittest.mock import Mock
from LearningCourse.Unit_Testing.DevelopmentCode import odometer

class TestOdometer(TestCase):
    def test_alert_normal(self):
        odometer.speed=Mock()
        odometer.speed.return_value = 90
        self.assertFalse(odometer.alert())

    def test_alert_overspeed(self):
        odometer.speed = Mock()
        odometer.speed.return_value = 100
        self.assertFalse(odometer.alert())

    def test_alert_underspeed(self):
        odometer.speed = Mock()
        odometer.speed.return_value = 59
        self.assertTrue(odometer.alert())