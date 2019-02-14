import unittest
from cipher import sub_cipher


class CipherTests(unittest.TestCase):
    """
    Run several error tests
    """

    def test_one_to_one(self):
        self.assertTrue(sub_cipher('toot', 'peep'))

    def test_one_to_two_correspondence(self):
        self.assertFalse(sub_cipher('lambda', 'school'))

    def test_two_to_one_correspondence(self):
        self.assertFalse(sub_cipher('school', 'lambda'))

    def test_unequal_length(self):
        self.assertFalse(sub_cipher('o', 'lambda'))

    def test_empty_strings(self):
        self.assertTrue(sub_cipher('', ''))


if __name__ == '__main__':
    unittest.main()
