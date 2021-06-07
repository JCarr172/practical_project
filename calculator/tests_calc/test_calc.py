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
        statline = {"stren":15,
                "dex":14, 
                "con":13, 
                "wis":12, 
                "intel":10,
                "char":8}
        response = self.client.post(url_for("change_stats"), json={"race":'Human','stats':statline})
        self.assertEqual(response.status_code, 200)
        self.assertIn('"dex":15',response.data.decode('utf-8'))

    def test_highelf_stats(self):
        statline = {"stren":15,
                "dex":14, 
                "con":13, 
                "wis":12, 
                "intel":10,
                "char":8}
        response = self.client.post(url_for("change_stats"), json={"race":'High Elf','stats':statline})
        self.assertEqual(response.status_code, 200)
        self.assertIn('"dex":16',response.data.decode('utf-8'))
        self.assertIn('"intel":11',response.data.decode('utf-8'))

    def test_mountaindwarf_stats(self):
        statline = {"stren":15,
                "dex":14, 
                "con":13, 
                "wis":12, 
                "intel":10,
                "char":8}
        response = self.client.post(url_for("change_stats"), json={"race":'Mountain Dwarf','stats':statline})
        self.assertEqual(response.status_code, 200)
        self.assertIn('"stren":17',response.data.decode('utf-8'))
        self.assertIn('"con":14',response.data.decode('utf-8'))

    def test_lightfoothalfling_stats(self):
        statline = {"stren":15,
                "dex":14, 
                "con":13, 
                "wis":12, 
                "intel":10,
                "char":8}
        response = self.client.post(url_for("change_stats"), json={"race":'Lightfoot Halfling','stats':statline})
        self.assertEqual(response.status_code, 200)
        self.assertIn('"dex":16',response.data.decode('utf-8'))
        self.assertIn('"char":9',response.data.decode('utf-8'))

    def test_dragonborn_stats(self):
        statline = {"stren":15,
                "dex":14, 
                "con":13, 
                "wis":12, 
                "intel":10,
                "char":8}
        response = self.client.post(url_for("change_stats"), json={"race":'Dragonborn','stats':statline})
        self.assertEqual(response.status_code, 200)
        self.assertIn('"stren":17',response.data.decode('utf-8'))
        self.assertIn('"char":9',response.data.decode('utf-8'))