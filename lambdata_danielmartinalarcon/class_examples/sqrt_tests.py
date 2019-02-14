import unittest
from scratch import *


class SqrtTests(unittest.TestCase):
    """Obligatory docstring"""

    def test_sqrt9(self):
        self.assertEqual(newton_sqrt1(9), 3)

    def test_sqrt2(self):
        self.assertAlmostEqual(newton_sqrt1(2), .41421356237)

if __name__ == '__main__':
    unittest.main()
