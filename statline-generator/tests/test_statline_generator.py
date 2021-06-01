from flask import url_for
from flask_testing import TestCase
import requests_mock
from unittest.mock import patch

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_human_stats(self):
        with patch('random.randint') as r:
            r = 0
            response = self.client.post(url_for("stats"), json={"race":'Human'})
            self.assertEqual(response.status_code, 200)
            self.assertIn('"char":16',response.data.decode('utf-8'))

    def test_highelf_stats(self):
        with patch('random.randint') as r:
            r = 0
            response = self.client.post(url_for("stats"), json={"race":'High Elf'})
            self.assertEqual(response.status_code, 200)
            self.assertIn('"dex":15',response.data.decode('utf-8'))

    def test_mountaindwarf_stats(self):
        with patch('random.randint') as r:
            r = 0
            response = self.client.post(url_for("stats"), json={"race":'Mountain Dwarf'})
            self.assertEqual(response.status_code, 200)
            self.assertIn('"stren":16',response.data.decode('utf-8'))

    def test_lightfoothalfling_stats(self):
        with patch('random.randint') as r:
            r = 0
            response = self.client.post(url_for("stats"), json={"race":'Lightfoot Halfling'})
            self.assertEqual(response.status_code, 200)
            self.assertIn('"dex":15',response.data.decode('utf-8'))

    def test_dragonborn_stats(self):
        with patch('random.randint') as r:
            r = 0
            response = self.client.post(url_for("stats"), json={"race":'Dragonborn'})
            self.assertEqual(response.status_code, 200)
            self.assertIn('"char":16',response.data.decode('utf-8'))