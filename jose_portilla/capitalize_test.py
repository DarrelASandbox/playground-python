import unittest
import capitalize 

class TestCapitalizeText(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = capitalize.capitalize_text(text)
        self.assertEqual(result, 'Python')

    def test_multiple_words(self):
        text = 'python has an elephant'
        result = capitalize.capitalize_text(text)
        self.assertEqual(result, 'Python Has An Elephant') 

if __name__ == '__main__':
    unittest.main()
