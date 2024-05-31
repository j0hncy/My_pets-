import unittest
from petsclass import Cat  # Import your Cat class from your file

class TestCat(unittest.TestCase):
    def setUp(self):
        self.cat = Cat()  # Create an instance of Cat for testing
    
    def test_initial_age(self):
        # Assert that the cat's initial age is within the range of 5 to 10
        self.assertTrue(5 <= self.cat.getAge() <= 10)

    def test_speak_method(self):
        # Test speak method with message
        response = self.cat.speak("Hello")
        self.assertEqual(response, "kitty says: Hello")

        # Test speak method without message
        response = self.cat.speak()
        self.assertEqual(response, "kitty says: meow")

if __name__ == '__main__':
    unittest.main()