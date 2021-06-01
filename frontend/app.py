#from models import Character
from flask import render_template, request, redirect, url_for, Flask
from flask_sqlalchemy import SQLAlchemy
import os
import requests
import random

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SECRET_KEY'] = os.getenv('SECRET')

db = SQLAlchemy(app)
class Character(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    race = db.Column(db.String(30), nullable = False)
    class_ = db.Column(db.String(30), nullable = False)
    strength = db.Column(db.Integer, nullable = False)
    dex = db.Column(db.Integer, nullable = False)
    con = db.Column(db.Integer, nullable = False)
    wis = db.Column(db.Integer, nullable = False)
    intelligence = db.Column(db.Integer, nullable = False)
    charisma = db.Column(db.Integer, nullable = False)


@app.route('/')
@app.route('/home')
def home():
     all_chars = Character.query.order_by(Character.id.desc()).limit(5).all()
     return render_template('home.html', all_chars = all_chars)

@app.route('/creater')
def creater():
     race = requests.get('http://race-generator:5000/get_race')
     class_ = requests.get('http://class-generator:5000/get_class')
     statline = requests.post('http://statline-generator:5000/get_stats', json={"race":race.text})
     new_char = Character(race = race.text,
               class_= class_.text,
               strength = statline.json()["stren"],
               dex = statline.json()["dex"],
               con = statline.json()["con"],
               wis = statline.json()["wis"],
               intelligence = statline.json()["intel"],
               charisma = statline.json()["char"])
     db.session.add(new_char)
     db.session.commit()
     return redirect(url_for("home"))

     
if __name__ =="__main__":
    app.run(debug=True, host='0.0.0.0')