from flask import Flask, jsonify
from flask import request
from lib.website import Website
import json
import time


app = Flask(__name__)

global website, lastUpdated
lastUpdated = time.time()
website = Website()


@app.route("/classinfo", methods=["POST"])
def classinfo():
    updateDB()
    subjcode = request.form['classname'].upper()
    result = website.getClassInfo(subjcode)
    return jsonify(result.getDict()) if result != None else "No class information available"

@app.route("/roominfo", methods=["POST"])
def roominfo():
    updateDB()
    room = request.form['room'].upper()
    result = website.getRoomInfo(room)
    # result is a list of classes
    if len(result) > 0:
        resultJson = jsonify([i.getDict() for i in result])
        # return resultJson
        return result[0]
    else:
        return "No room information available"

@app.route("/getclasses", methods=["POST"])
def getclasses():
    updateDB()
    codes = request.form['codes'].split(',')
    if len(codes) == 0:
        return "No subject codes given"
    else:
        result = website.getClasses(codes)
        resultJson = jsonify([i.getDict() for i in result])
        return resultJson

# TODO handle incorrect API calls or parameter

def updateDB():
    global lastUpdated, website
    now = time.time()
    if now - lastUpdated >= 1800:
        # meaning 30 minutes have passed
        del website
        website = Website()
        # starts the parsing process again
        lastUpdated = now
        # update the last updated time

@app.route("/getclasses", methods=["POST"])
def getClasses():
    updateDB()
    codes = request.form["codes"].split(",")
    result = website.getClasses(codes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
