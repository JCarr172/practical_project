from flask import Flask, request
import random

app = Flask(__name__)

@app.route('/get_class', methods = ['GET'])
def classes():
    return random.choice(['Fighter', 'Wizard', 'Ranger', 'Cleric', 'Sorcerer', 'Barbarian'])

if __name__ =="__main__":
    app.run(debug=True, host='0.0.0.0')