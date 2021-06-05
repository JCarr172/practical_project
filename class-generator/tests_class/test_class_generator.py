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
        self.assertIn(data['class'],['fighter', 'wizard', 'ranger', 'cleric', 'sorcerer', 'barbarian','warlock'])
        self.assertIn(data['race'],['human', 'high elf', 'mountain dwarf', 'lightfoot halfling', 'dragonborn'])