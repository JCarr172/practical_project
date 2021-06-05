from flask import Flask, request, jsonify
import random
import requests

app = Flask(__name__)

@app.route('/change_stats', methods = ['GET','POST'])
def change_stats():
    race = request.get_json()["race"]
    name = request.get_json()["name"]
    standard_stats=[15, 14, 13, 12, 10, 8]
    strength = request.get_json()['stats']['stren']
    dext = request.get_json()['stats']['dex']
    const = request.get_json()['stats']['con']
    wisd = request.get_json()['stats']['wis']
    intelli = request.get_json()['stats']['intel']
    charisma = request.get_json()['stats']['char']
    if race == 'high elf':
        name = (name + " the elegant")
        dext +=2
        intelli +=1
    elif race == 'mountain dwarf':
        name = name + (" the strong")
        strength +=2
        const +=1
    elif race == 'lightfoot halfling':
        name = name + (" the witty")
        charisma +=1
        dext +=2
    elif race == 'dragonborn':
        name = name + (" the fierce")
        strength +=2
        charisma +=1
    else:
        name = name + (" the brave")
        strength +=1
        dext +=1
        const +=1
        wisd +=1
        intelli +=1
        charisma +=1
    statline = {"name":name,
                "stren":strength,
                "dex":dext, 
                "con":const, 
                "wis":wisd, 
                "intel":intelli,
                "char":charisma}
    return jsonify(statline)

if __name__ =="__main__":
    app.run(debug=True, host='0.0.0.0')  # pragma: no cover