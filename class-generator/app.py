from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/get_class', methods = ['GET','POST'])
def classes():
    race = random.choice(['human', 'high elf', 'mountain dwarf', 'lightfoot halfling', 'dragonborn'])
    class_ = random.choice(['fighter', 'wizard', 'ranger', 'cleric', 'sorcerer', 'barbarian','warlock'])
    return jsonify({'race':race,'class':class_})

if __name__ =="__main__":
    app.run(debug=True, host='0.0.0.0')  # pragma: no cover