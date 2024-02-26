import pytest
import unittest
from uuid import UUID
import uuid

from category import Category


class TestCategory(unittest.TestCase):
    def test_name_is_required(self):
        with pytest.raises(TypeError, match="missing 1 required positional argument: 'name'"):
            Category()
    
    def test_must_have_than_255_characters(self):
        with pytest.raises(ValueError, match="name must have less than 256 characters"):
            Category(name="a"*256)
    
    def test_category_must_be_created_with_id_as_uuid(self):
        category = Category(name="Filme")
        assert isinstance(category.id, UUID)
                
    def test_created_category_with_default_values(self):
        category = Category(name="Filme")
        assert category.name == "Filme"
        assert category.description == ""
        assert category.is_active == True
    
    def test_category_is_created_as_active_by_default(self):
        
        category = Category(name="Filme")
        assert category.is_active == True
    
    def test_category_is_created_with_provided_values(self):
        cat_id = uuid.uuid4()
        category = Category(
            id=cat_id,
            name="Filme",
            description="Filmes em Geral",
            is_active=False,
        )
        
        self.assertEqual(category.id, cat_id)
        self.assertEqual(category.name, "Filme")
        self.assertEqual(category.description, "Filmes em Geral")
        self.assertEqual(category.is_active, False)
        
        
        
        
        
        
if __name__ == "__main__":
    unittest.main()
    

