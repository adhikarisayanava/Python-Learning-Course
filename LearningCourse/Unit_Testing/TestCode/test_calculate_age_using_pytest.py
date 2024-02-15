import pytest
from LearningCourse.Unit_Testing.DevelopmentCode.calculate_age import get_age
from datetime import date
from unittest import TestCase

class TestUnitTesting(TestCase):
    def test_get_age_usingunittest(self):
        # This test is written using unittest
        self.assertEqual(get_age(date(1990, 1, 1)), 34)

def test_get_age_1():
    # Test case 1: Valid input, this test is written using pytest
    assert get_age(date(1990, 1, 1)) == 34

def test_get_age_2():
    # Test case 2: Future year
    with pytest.raises(ValueError):
        assert get_age(date(2050, 1, 1)) == 0

def test_get_age_3():
    # Test case 3: Negative year
    with pytest.raises(ValueError):
        get_age(date(-1990, 1, 1))

def test_get_age_4():
    # Test case 4: Current year
    assert get_age(date(2024, 1, 1)) == 0

def test_get_age_5():
    # Test case 5: Leap year
    assert get_age(date(2000, 1, 1)) == 24

def test_get_age_6():
    # Test case 6: Birth year in the future
    with pytest.raises(ValueError):
        get_age(date(2025, 1, 1))

def test_get_age_7():
    # Test case 7: Birth year in the distant past
    with pytest.raises(ValueError):
        get_age(date(1000, 1, 1))
