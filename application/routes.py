from application import app, db
#from application.models import 
from flask import render_template, request, redirect, url_for
#from application.forms import


@app.route('/')
@app.route('/home')
def home():
     return "Hello World"