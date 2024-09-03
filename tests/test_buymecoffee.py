import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

from src.buy_me_coffee.buymecoffee import ButMeCoffee

class TestCalculations(unittest.TestCase):

    def test_supporters(self):
        buymecoffee = ButMeCoffee()
        result = buymecoffee.get_supporters()
        self.assertEqual(result.get("test"), "someStr", 'The result is wrong.')

if __name__ == '__main__':
    unittest.main()