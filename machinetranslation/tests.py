import unittest
from translator import english_to_french, french_to_english

class TestE2F(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french(None), None, 'None should return None')
        self.assertEqual(english_to_french("Hello"), "Bonjour", "Hello should be translated to Bonjour")
        self.assertNotEqual(english_to_french("Goodbye"), "Chaise", "Goodbye should not be translated to Chaise")
        self.assertEqual(english_to_french("Goodbye"), "Au revoir", "Goodbye should be translated to Au revoir")

class TestF2E(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english(None), None, 'None should return None')
        self.assertEqual(french_to_english("Bonjour"), "Hello", "Bonjour should be translated to Hello")
        self.assertNotEqual(french_to_english("Au revoir"), "Chair", "Au revoir should not be translated to Chair")
        self.assertEqual(french_to_english("Au revoir"), "Goodbye", "Au revoir should be translated to Goodbye")

unittest.main()