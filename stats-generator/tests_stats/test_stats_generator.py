from flask import url_for
from flask_testing import TestCase
import requests_mock
from unittest.mock import patch

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_class(self):
        with patch('random.randint') as r:
            r = 0
            response = self.client.post(url_for("get_stats"))
            self.assertEqual(response.status_code, 200)
            self.assertIn('"char":15',response.data.decode('utf-8'))