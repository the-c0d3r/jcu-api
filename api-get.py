from flask import Flask, jsonify
from flask import request
from lib.website import Website
import json
import time


app = Flask(__name__)

global website, lastUpdated
lastUpdated = time.time()
website = Website()


@app.route("/classinfo")
def classinfo():
    updateDB()
    subjcode = request.args.get('classname').upper()
    result = website.getClassInfo(subjcode)

    if result == None:
        return jsonify({"count":0})
    else:
        resultJson = {
            "count": 1,
            "result": [result.getDict()]
        }
        print(resultJson)
        return jsonify(resultJson)

@app.route("/roominfo")
def roominfo():
    updateDB()
    room = request.args.get('room').upper()
    result = website.getRoomInfo(room)
    resultJson = {
        "count": len(result),
        "result": []
        }
    # result is a list of classes
    if len(result) > 0:
        for cl in result:
            resultJson["result"].append(cl.getDict())
        return jsonify(resultJson)
    else:
        return jsonify({"count": 0})

@app.route("/getclasses")
def getclasses():
    updateDB()
    codes = request.args.get('codes').split(',')
    if len(codes) == 0:
        return "No subject codes given"
    else:
        result = website.getClasses(codes)
        if len(result) == 0:
            return jsonify({"count":0})
        else:
            resultJson = {
                "count": len(result),
                "result": []
            }
            for cl in result:
                resultJson["result"].append(cl.getDict())
            return jsonify(resultJson)

# TODO handle incorrect API calls or parameter

def updateDB():
    global lastUpdated, website
    now = time.time()
    # if now - lastUpdated >= 1800:
    if now - lastUpdated >= 1800:
        # meaning 30 minutes have passed
        del website
        website = Website()
        # starts the parsing process again
        lastUpdated = now
        # update the last updated time

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
