from app import app
from flask import render_template
import requests
import json
import sonoff

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

    # get device status as json
    response3 = requests.get("https://smarteff.herokuapp.com/ListDeviceStatus")
    response3 = response3.text
    device_status = json.loads(response3)

    # person array to redirect
    persons = []

    # append person names to the list
    for person in loaded['people']:
        persons.append(person['name'])

    return render_template("office.html", persons=persons, devices=devices, device_status=device_status, loaded=loaded)

# simulation view 
@app.route("/simulate", methods=['POST','GET'])
def simulate():

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

    # get device status as json
    response3 = requests.get("https://smarteff.herokuapp.com/ListDeviceStatus")
    response3 = response3.text
    device_status = json.loads(response3)

    # person array to redirect
    persons = []

    # append person names to the list
    for person in loaded['people']:
        persons.append(person['name'])

    return render_template("simulation.html", persons=persons, devices=devices, device_status=device_status, loaded=loaded)

# device manager view
@app.route('/ManageDevices')
def manage_devices():
    s = sonoff.Sonoff("denguner5@gmail.com","smarteff","us")
    devices = s.get_devices()
    return render_template("ingdog.html", sayfabasligi="Main Page",devicelist=devices,deviceid=1)

# show current device status
@app.route('/ShowDeviceStatus')
def dev_status():
    s = sonoff.Sonoff("denguner5@gmail.com","smarteff","us")
    devices = s.get_devices()
    return render_template("never.html", kablolubaglanti="Monitoring",devicelist=devices,deviceid=1)     