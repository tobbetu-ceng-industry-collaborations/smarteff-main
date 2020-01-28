from app import app
from flask import render_template

# show current event log under the route /log
@app.route("/log", methods=['POST','GET'])
def log():

	# read event history file
    event_log = open('event_history.log', "r")
    content = event_log.read()

    return render_template("log.html", log=content)
