from app import app
from app import db

from app.models import *

# import jsonify to make form conversions easy
from flask import jsonify

# import request to fetch the information about events
from flask import request

import logging

logging.basicConfig(filename='event_history.log', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.WARNING)

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
        logging.warning('[person_event]A person(id=%s) has entered!', str(person_id))
    elif event == 'exit':
        person.is_inside = 0;
        logging.warning('[person_event]A person(id=%s) has left!', str(person_id))

        # TODO
        # (1) check person's devices
        # (2) check assigned persons 

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

    # get device or throw 404
    device = Device.query.get_or_404(device_id)

    # change is_on status according to event
    if event == 'turnon':
        device.is_on = 1;
        logging.warning('[device_event]A device(id=%s) has turned on!', str(device_id))
    elif event == 'turnoff':
        device.is_on = 0;
        logging.warning('[device_event]A device(id=%s) has turned off!', str(device_id))

    # write changes to DB
    db.session.add(device)
    db.session.commit()

    # prepare the response --> assuming everything is OK
    resp = jsonify({'success':True})

    return resp, 200

