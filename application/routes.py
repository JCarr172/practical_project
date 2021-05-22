from application import app, db
#from application.models import 
from flask import render_template, request, redirect, url_for
#from application.forms import
import random


@app.route('/')
@app.route('/home')
def home():
     return render_template('home.html')

@app.route('/creator')
def creator():
     races = ['Human', 'Elf', 'Dwarf', 'Halfling', 'Dragonborn', 'Half-elf']
     race = races[random.randint(0,5)]
     classes = ['Fighter', 'Wizard', 'Ranger', 'Cleric', 'Sorcerer', 'Barbarian']
     class_ = classes[ramdom.randint(0,5)]
     strength = random.randint(6,15)
     dex = random.randint(6,15)
     con = random.randint(6,15)
     wis = random.randint(6,15)
     intelligence = random.randint(6,15)
     charisma = random.randint(6,15)
     return redirect(url_for("home"))