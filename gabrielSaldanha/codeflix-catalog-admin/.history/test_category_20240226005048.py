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
        with pytest.raises(ValueError, match="name cannot be longer than 255 characters"):
            Category(name="a"*256)
    
    def test_category_must_be_created_with_id_as_uuid(self):
        category = Category(name="Filme")
        assert isinstance(category.id, UUID)
                
    def test_created_category_with_default_values(self):
        category = Category(name="Filme")
        assert category.name == "Filme"
        assert category.description == ""
        assert category.is_active is True
    
    def test_category_is_created_as_active_by_default(self):
        
        category = Category(name="Filme")
        assert category.is_active is True
    
    def test_category_is_created_with_provided_values(self):
        cat_id = uuid.uuid4()
        category = Category(
            id=cat_id,
            name="Filme",
            description="Filmes em Geral",
            is_active=False,
        )
        
        assert category.id == cat_id
        assert category.name == "Filme"
        assert category.description == "Filmes em Geral"
        assert category.is_active is False
        
    def test_cannot_create_category_with_empty_name(self):
        with pytest.raises(ValueError, math="name cannot be empty"):
            Category(name="")


class TestUpdateCategory:
    def test_update_category_with_name_and_description(self):
        category = Category(name="Filme", description="Filmes em Geral")
        
        # Realização do teste simulando a  Alteração
        category.update_category(name="Série", description="Séries em Geral")
        
        assert category.name == "Série"
        assert category.description == "Séries em Geral"
              
    def test_update_category_with_invalid_name_raises_exception(self):
        category = Category(name="Filme", description="Filmes em Geral")
        
        with pytest.raises(ValueError, match="name cannot be longer than 255 characters"):
            category.update_category(name="a" * 256, description="Séries em Geral")
            

                
            