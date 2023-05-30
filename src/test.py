from text import to_upper, to_word_list_isupper
import unittest

class TestAddition(unittest.TestCase):

    def test_is_upper(self):
        self.assertEqual(to_upper("abcdef"), "ABCDEF")

    def test_list_is_upper(self):
        self.assertTrue(to_word_list_isupper(['I', 'LOVE', 'YOU']), True)

    def test_list_isnt_upper(self):
        self.assertFalse(to_word_list_isupper(['i', 'LOVE', 'YOU']), False)

    def test_type_upper(self):
        with self.assertRaises(TypeError):
            to_upper()

    def test_type_list_upper(self):
        with self.assertRaises(TypeError):
            to_word_list_isupper()
    

if __name__ == '__main__':
    unittest.main()