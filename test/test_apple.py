import unittest
import apples


class MyTestCase(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    def test_apple_color(self):
        # Tests that work for only a certain version of the library.
        self.assertEqual("red", apples.get_apple_color())

    def test_apple_color_with_change(self):
        # Tests that work for only a certain version of the library.
        self.assertEqual("red", apples.get_apple_color())
        apples.change_apple_color("blue")
        self.assertEqual("blue", apples.get_apple_color())
