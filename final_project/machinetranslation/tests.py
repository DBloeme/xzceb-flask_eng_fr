import unittest
from translator import english_to_french,french_to_english

class test_Translator_e2f(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertNotEqual(english_to_french("None"), '')
        self.assertNotEqual(english_to_french(0), 0)
        self.assertEqual(english_to_french('Thank you'), 'Je vous remercie')
        self.assertEqual(english_to_french('Goodbye'), 'Au revoir')

class test_Translator_f2e(unittest.TestCase):
    def test_frenchToEnglish(self):
        self.assertNotEqual(french_to_english("None"), '')
        self.assertNotEqual(french_to_english(0), 0)
        self.assertEqual(french_to_english('Je vous remercie'), 'Thank you')

if __name__ == "__main__":
    unittest.main