from unittest import TestCase
from main_hw import MainHW


class MainHWTest(TestCase):
    def test_is_even(self):
        self.assertTrue(MainHW.is_even(4))
        self.assertFalse(MainHW.is_even(7))
        self.assertTrue(MainHW.is_even(0))
        self.assertTrue(MainHW.is_even(-2))
        self.assertFalse(MainHW.is_even(-3))

    def test_is_in_range(self):
        self.assertTrue(MainHW.is_in_range(50))
        self.assertFalse(MainHW.is_in_range(10))
        self.assertFalse(MainHW.is_in_range(150))
        self.assertFalse(MainHW.is_in_range(25))
        self.assertFalse(MainHW.is_in_range(100))
