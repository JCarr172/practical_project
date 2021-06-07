from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/get_class', methods = ['GET','POST'])
def classes():
    race = random.choice(['Human', 'High Elf', 'Mountain Dwarf', 'Lightfoot Halfling', 'Dragonborn'])
    class_ = random.choice(['Fighter', 'Wizard', 'Ranger', 'Cleric', 'Sorcerer', 'Barbarian','Warlock'])
    return jsonify({'race':race,'class':class_})

if __name__ =="__main__":
    app.run(debug=True, host='0.0.0.0')  # pragma: no cover