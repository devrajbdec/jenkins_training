import unittest

from weather import get_will_rain


class TestWeather(unittest.TestCase):

    def test_weather(self):
        # Tests that work for only a certain version of the library.
        self.assertTrue(get_will_rain())