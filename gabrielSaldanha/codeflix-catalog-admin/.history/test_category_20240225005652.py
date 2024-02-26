import unittest # std - Ja vem Instalada com o python

from category import Category


class TestCategory(unittest.TestCase):
    def test_name_is_required(self):
        with self.assertRaises(TypeError):
            print("Oi")
        
        
if __name__ == "__main__":
    unittest.main()
    

