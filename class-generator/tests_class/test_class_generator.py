from flask import url_for
from flask_testing import TestCase
import requests_mock

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_class(self):
        response = self.client.get(url_for("classes"))
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn(data['class'],['Fighter', 'Wizard', 'Ranger', 'Cleric', 'Sorcerer', 'Barbarian','Warlock'])
        self.assertIn(data['race'],['Human', 'High Elf', 'Mountain Dwarf', 'Lightfoot Halfling', 'Dragonborn'])