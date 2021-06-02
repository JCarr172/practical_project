from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/get_stats', methods = ['GET','POST'])
def stats():
    standard_stats=[15, 14, 13, 12, 10, 8]
    strength = standard_stats.pop(random.randint(0,5))
    dext = standard_stats.pop(random.randint(0,4))
    const = standard_stats.pop(random.randint(0,3))
    wisd = standard_stats.pop(random.randint(0,2))
    intelli = standard_stats.pop(random.randint(0,1))
    charisma = standard_stats.pop()
    statline = {"stren":strength,
                "dex":dext, 
                "con":const, 
                "wis":wisd, 
                "intel":intelli,
                "char":charisma}
    return jsonify({'stats':statline})

if __name__ =="__main__":
    app.run(debug=True, host='0.0.0.0')