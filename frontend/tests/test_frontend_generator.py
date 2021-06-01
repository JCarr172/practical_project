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

class TestHome(TestBase):
    def test_create(self):
        with requests_mock.Mocker() as mocker:
            mocker.get('http://race-generator:5000/get_race', text='Human')
            mocker.get('http://class-generator:5000/get_class', text='Wizard')
            mocker.post('http://statline-generator:5000/get_stats', json={'stren':15,'dex':14,'con':13,'wis':8,'intel':16,'char':10})
            response = self.client.get(url_for("creater"),follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Your character is a human wizard', response.data)