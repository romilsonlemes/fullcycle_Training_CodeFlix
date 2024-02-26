import unittest # std - Ja vem Instalada com o python

from category import Category


class TestCategory(unittest.TestCase):
    def test_name_is_required(self):
        with self.assertRaises(TypeError):
        

