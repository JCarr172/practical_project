from flask import Flask, request, jsonify
import random
import requests

app = Flask(__name__)

@app.route('/get_stats', methods = ['POST'])
def stats():
    race = request.get_json()["race"]
    standard_stats=[15, 14, 13, 12, 10, 8]
    strength = standard_stats.pop(random.randint(0,5))
    dext = standard_stats.pop(random.randint(0,4))
    const = standard_stats.pop(random.randint(0,3))
    wisd = standard_stats.pop(random.randint(0,2))
    intelli = standard_stats.pop(random.randint(0,1))
    charisma = standard_stats.pop()
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
    app.run(debug=True, host='0.0.0.0')