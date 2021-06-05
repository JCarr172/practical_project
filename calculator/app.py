from flask import Flask, request, jsonify
import random
import requests

app = Flask(__name__)

@app.route('/change_stats', methods = ['GET','POST'])
def change_stats():
    race = request.get_json()["race"]
    standard_stats=[15, 14, 13, 12, 10, 8]
    strength = request.get_json()['stats']['stren']
    dext = request.get_json()['stats']['dex']
    const = request.get_json()['stats']['con']
    wisd = request.get_json()['stats']['wis']
    intelli = request.get_json()['stats']['intel']
    charisma = request.get_json()['stats']['char']
    if race == 'High Elf':
        dext +=2
        intelli +=1
    elif race == 'Mountain Dwarf':
        strength +=2
        const +=1
    elif race == 'Lightfoot Halfling':
        charisma +=1
        dext +=2
    elif race == 'Dragonborn':
        strength +=2
        charisma +=1
    else:
        strength +=1
        dext +=1
        const +=1
        wisd +=1
        intelli +=1
        charisma +=1
    statline = {"stren":strength,
                "dex":dext, 
                "con":const, 
                "wis":wisd, 
                "intel":intelli,
                "char":charisma}
    return jsonify(statline)

if __name__ =="__main__":
    app.run(debug=True, host='0.0.0.0')  # pragma: no cover