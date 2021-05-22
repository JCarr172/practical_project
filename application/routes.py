from application import app, db
from application.models import Character
from flask import render_template, request, redirect, url_for
#from application.forms import
import random


@app.route('/')
@app.route('/home')
def home():
     all_chars = Character.query.order_by(Character.id.desc()).limit(5).all()
     return render_template('home.html', all_chars = all_chars)

@app.route('/creator')
def creator():
     name = 'Test'
     races = ['Human', 'Elf', 'Dwarf', 'Halfling', 'Dragonborn', 'Half-elf']
     race = races[random.randint(0,5)]
     classes = ['Fighter', 'Wizard', 'Ranger', 'Cleric', 'Sorcerer', 'Barbarian']
     class_ = classes[random.randint(0,5)]
     strength = random.randint(8,15)
     dex = random.randint(8,15)
     con = random.randint(8,15)
     wis = random.randint(8,15)
     intelligence = random.randint(8,15)
     charisma = random.randint(8,15)
     new_char = Character(name=name,
               race = race,
               class_= class_,
               strength = strength,
               dex = dex,
               con = con,
               wis = wis,
               intelligence = intelligence,
               charisma = charisma)
     db.session.add(new_char)
     db.session.commit()
     return redirect(url_for("home"))