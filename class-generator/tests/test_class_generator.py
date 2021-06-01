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
        self.assertEqual(response.status_code, 200)
        self.assertIn(response.data.decode('utf-8'),['Fighter', 'Wizard', 'Ranger', 'Cleric', 'Sorcerer', 'Barbarian'])