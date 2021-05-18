from application import db

class Character(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), nullable = False)
    race = db.Column(db.String(30), nullable = False)
    class_ = db.Column(db.String(30), nullable = False)
    strength = db.Column(db.Integer, nullable = False)
    dex = db.Column(db.Integer, nullable = False)
    con = db.Column(db.Integer, nullable = False)
    wis = db.Column(db.Integer, nullable = False)
    intelligence = db.Column(db.Integer, nullable = False)
    charisma = db.Column(db.Integer, nullable = False)