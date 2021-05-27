from flask import Flask, request
import random

app = Flask(__name__)

@app.route('/get_stats', methods = ['POST'])
def stats():
    strength = random.randint(8,15)
    dex = random.randint(8,15)
    con = random.randint(8,15)
    wis = random.randint(8,15)
    intel = random.randint(8,15)
    char = random.randint(8,15)
    if request.data.decode('utf-8') == 'HighElf':
        dex +=2
        intel +=1
    elif request.data.decode('utf-8') == 'Mountain Dwarf':
        strength +=2
        con +=1
    elif request.data.decode('utf-8') == 'Lightfoot Halfling':
        char +=1
        dex +=2
    elif request.data.decode('utf-8') == 'Dragonborn':
        strength +=2
        char +=1
    else:
        strength +=1
        dex +=1
        con +=1
        wis +=1
        intel +=1
        char +=1
    return strength, dex, con, wis, intel, char

if __name__ =="__main__":
    app.run(debug=True, host='0.0.0.0')