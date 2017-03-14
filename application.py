from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

current_year = datetime.now().year

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template('Index.html')

@app.route("/outdoor", methods=["GET", "POST"])
def outdoor():
    return render_template("outdoor.html")

@app.route("/indoor", methods=["GET", "POST"])
def indoor():
    return render_template("indoor.html")

@app.route("/xc", methods=["GET", "POST"])
def xc():
    return render_template("xc.html")

@app.route("/outdoor/outdoorschedule")
def outdoor_schedule():
    #show all current_year meets (todo)
    return render_template("outdoorschedule.html", current_year = current_year)

@app.route("/indoor/indoorschedule")
def indoor_schedule():
    if datetime.now().month < 4:
        indcurrent_year = current_year - 1
    else:
        indcurrent_year = current_year
    #show all meets for indcurrent_year - indcurrent_year - 1 (todo)
    return render_template("indoorschedule.html", current_year = indcurrent_year)

@app.route("/xc/xcschedule")
def xc_schedule():

    return render_template("xcschedule.html", current_year = xccurrent_year)
