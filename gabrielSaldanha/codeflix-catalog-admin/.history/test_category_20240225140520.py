import unittest
from uuid import UUID

from category import Category


class TestCategory(unittest.TestCase):
    def test_name_is_required(self):
        with self.assertRaisesRegex(TypeError, "missing 1 required positional argument: 'name'"):
            Category()
    
    def test_must_have_than_255_characters(self):
        with self.assertRaisesRegex(ValueError, "name must have less than 256 characters"):
            Category(name="a"*256)
    
    def test_category_must_be_created_with_id_as_uuid(self):
        category = Category(name="Filme")
        self.assertEqual(type(category.id), UUID)
        
    def test_created_category_with_default_values(self):
        
    
if __name__ == "__main__":
    unittest.main()
    

