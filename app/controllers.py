from app import app
from app import db

from app.models import *

# import jsonify to make form conversions easy
from flask import jsonify

# import request to fetch the information about events
from flask import request

# endpoint to handle person events
@app.route("/HandlePersonEvent", methods=['POST'])
def person_event():

    # parse http request body
    data = request.json
    person_id= data['personid']
    event = data['event']

    # get person or throw 404
    person = Person.query.get_or_404(person_id)

    # change is_inside status according to event
    if event == 'entry':
        person.is_inside = 1;
    elif event == 'exit':
        person.is_inside = 0;

    # write changes to DB
    db.session.add(person)
    db.session.commit()

    # prepare the response --> assuming everything is OK
    resp = jsonify({'success':True})

    return resp, 200

# endpoint to handle device events
@app.route("/HandleDeviceEvent", methods=['POST'])
def device_event():

    # parse http request body
    data = request.json
    device_id= data['deviceid']
    event = data['event']

    # get person or throw 404
    device = Device.query.get_or_404(device_id)

    # change is_on status according to event
    if event == 'turnon':
        device.is_on = 1;
    elif event == 'turnoff':
        device.is_on = 0;

    # write changes to DB
    db.session.add(device)
    db.session.commit()

    # prepare the response --> assuming everything is OK
    resp = jsonify({'success':True})

    return resp, 200

