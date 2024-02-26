import unittest # std - Ja vem Instalada com o python

from category import Category


class TestCategory(unittest.TestCase):
    def test_name_is_required(self):
        with self.assertRaisesRegex(TypeError, "missing 1 required positional argument: 'name'"):
            Category()
    
    def test_must_have_than_255_characters(self):
        with self.assertRaisesRegex(ValueError, "name must have less than 255 characters"):
            Category("a" * 254)
        
if __name__ == "__main__":
    unittest.main()
    
