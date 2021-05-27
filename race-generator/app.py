from flask import Flask, request
import random

app = Flask(__name__)

@app.route('/get_race', methods = ['GET'])
def race():
    return random.choice(['Human', 'High Elf', 'Mountain Dwarf', 'Lightfoot Halfling', 'Dragonborn'])

if __name__ =="__main__":
    app.run(debug=True, host='0.0.0.0')