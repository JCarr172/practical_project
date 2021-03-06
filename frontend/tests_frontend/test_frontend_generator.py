from flask import url_for
from flask_testing import TestCase
import requests_mock
import os

from app import app, db, Character

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI=os.getenv('TEST_DATABASE_URI'),
            SECRET_KEY=os.getenv('TEST_SECRET'),
            DEBUG=True,
            WTF_CSRF_ENABLED=False)
        return app
    
    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class Testcreate(TestBase):
    def test_create(self):
        with requests_mock.Mocker() as mocker:
            mocker.get('http://stats-generator:5000/get_stats', json={'stats':{'stren':15,'dex':14,'con':13,'wis':8,'intel':16,'char':10}})
            mocker.get('http://class-generator:5000/get_class', json={'race':'Human','class':'Wizard'})
            mocker.post('http://calculator:5000/change_stats', json={'name':'Caleb the brave','stren':15,'dex':14,'con':13,'wis':8,'intel':16,'char':10})
            response = self.client.get(url_for("creater", name = 'Caleb'),follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Caleb the brave is a Human Wizard', response.data)