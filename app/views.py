from app import app
from flask import render_template
import requests
import json

# show current event log under the route /log
@app.route("/log", methods=['POST','GET'])
def log():

	# read event history file
    event_log = open('event_history.log', "r")
    content = event_log.read()

    return render_template("log.html", log=content)

# admin view to define office layout
@app.route("/admin", methods=['POST','GET'])
def admin():

	# get person list as json
    response = requests.get("https://smarteff.herokuapp.com/ListPersons")
    response = response.text
    loaded = json.loads(response)

    # get person-device assignment as json
    response2 = requests.get("https://smarteff.herokuapp.com/ListPersonDeviceAssignment")
    response2 = response2.text
    devices_temp = json.loads(response2)
    
    # reverse dictionary
    devices = {v: k for k, v in devices_temp.items()}

    # person array to redirect
    persons = []

    # append person names to the list
    for person in loaded['people']:
        persons.append(person['name'])

    return render_template("office.html", persons=persons, devices=devices)

