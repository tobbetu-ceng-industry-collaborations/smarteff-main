from app import app
from app import db

from app.models import *

# import jsonify to make form conversions easy
from flask import jsonify

# import request to fetch the information about events
from flask import request

import logging

from datetime import datetime

# logger setup
logger = logging.getLogger('my-logger')
logger.propagate = False
logging.basicConfig(filename='event_history.log', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.WARNING)
logging.StreamHandler(stream=None)

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

# endpoint to manage device requests which will be redirected to component #6
@app.route("/ManageDevice", methods=['POST'])
def manage_device():

    # parse http request body
    data = request.json
    person_id= data['personid']
    device_id= data['deviceid']
    action = data['action']

    # get person or throw 404
    person = Person.query.get_or_404(person_id)

    # get device or throw 404
    device = Device.query.get_or_404(device_id)

    # redirect and log according to action
    if action == 'turnon':

        # TODO
        # (1) redirect to component #6

        logging.warning('[request_event]A person(id=%s) has requested a device(id=%s) to be turned on!', str(person_id), str(device_id))

    elif action == 'turnoff':

        # TODO
        # (1) redirect to component #6

        logging.warning('[request_event]A person(id=%s) has requested a device(id=%s) to be turned off!', str(person_id), str(device_id))


    # prepare the response --> assuming everything is OK
    resp = jsonify({'success':True})

    return resp, 200

# endpoint to suspend automation on a device for a person
@app.route("/SuspendAutomation", methods=['POST'])
def suspend_automation():

    # parse http request body
    data = request.json
    person_id= data['personid']
    device_id= data['deviceid']
    until = data['until']

    # get person or throw 404
    person = Person.query.get_or_404(person_id)

    # get device or throw 404
    device = Device.query.get_or_404(device_id)

    # parse the date
    dates = until.split('-')
    year = int(dates[0])
    month = int(dates[1])
    day = int(dates[2])
    hour = int(dates[3])
    minute = int(dates[4])
    second = int(dates[5])

    # TODO
    # (1) remove previous suspensions of the device since they are meaningless from now on.

    # insert suspension to table
    values = [person_id, device_id, datetime.now(), datetime(year, month, day, hour, minute, second)]
    insert_statement = suspension_request.insert().values(values)
    db.session.execute(insert_statement)
    db.session.commit()

    logging.warning('[automation_event]A person(id=%s) has requested a suspension for the automation of device(id=%s) until %s!', str(person_id), str(device_id), until)

    # prepare the response --> assuming everything is OK
    resp = jsonify({'success':True})

    return resp, 200


# endpoint to enable automation for a defined person
@app.route("/EnableAutomation", methods=['POST'])
def enable_automation():
	# parse http request body
    data = request.json
    person_id= data['personid']
    device_id= data['deviceid']

    # get person or throw 404
    person = Person.query.get_or_404(person_id)

    # get device or throw 404
    device = Device.query.get_or_404(device_id)

    # initialize new suspension list
    updated_suspensions = []

    # filter specified person's suspensions
    for suspension in device.suspensions:
    	if suspension == person:
    		continue
    	else:
    		updated_suspensions.append(suspension)


    # update new suspensions
    device.suspensions = updated_suspensions

    # write changes
    db.session.add(device)
    db.session.commit()    	


    logging.warning('[automation_event]A person(id=%s) has enabled automation of device(id=%s)', str(person_id), str(device_id))

    # prepare the response --> assuming everything is OK
    resp = jsonify({'success':True})

    return resp, 200

    

    # TODO
	# (1) Receive request
	# (2) Parse body
	# (3) Remove all previous suspension requets for the specified user



# -----------------------GET REQUEST ENDPOINTS---------------------------- 




# endpoint to list all persons
@app.route("/ListPersons", methods=['GET'])
def list_users():

    # get all persons
    persons = Person.query.all()

    # if persons are not empty, return person information in JSON format
    if persons is None:
        return make_response('There are no persons!', 400)
    return jsonify({'people': [person.serialize for person in persons]})

# endpoint to list devices of specified person with suspension information 
@app.route("/ListDevices/<person_id>", methods=['GET'])
def list_devices(person_id):

    # get person
    person = Person.query.get_or_404(person_id)
    
    # automation field templates to append
    automation_body1={
    	'suspend':"True",
    	'expiration':""
    }
    automation_body2={
    	'suspend':"False",
    }

    # response json
    response = []

    # for every device, check if there is any suspension, append information accordingly
    for device in person.devices:
        
        # fetch device info
        device_info = device.serialize
        device_id = device_info["id"]
        
        # check if there is any suspension for the device
        select_statement = db.select([suspension_request]).where(db.and_(suspension_request.c.person_id==person_id, suspension_request.c.device_id==device_id))
        query = db.session.execute(select_statement)

        # result
        query = query.first()

        # append automation body as json
        if query != None:
            expire_date = query.suspension_end
            automation_body3 = automation_body1
            automation_body3["expiration"] = expire_date
            device_info["automation"] = automation_body3
        else:
            device_info["automation"] = automation_body2
        
        # concat new information(automation) with device information
        response.append(device_info)

    # return json
    return jsonify({'devices': response})