from flask import Flask
from flask import request
from lib.website import Website


app = Flask(__name__)
website = Website()

@app.route("/classinfo", methods=["POST"])
def classinfo():
    subjcode = request.form['classname']
    result = website.getClassInfo(subjcode)

@app.route("/roominfo", methods=["POST"])
def roominfo():
    room = request.form['room']
    result = website.getRoomInfo(room)

@app.route("/getclasses", methods=["POST"])
def getClasses():
    codes = request.form["codes"].split(",")
    result = website.getClasses(codes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
