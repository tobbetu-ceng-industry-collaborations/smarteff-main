from app import app
from app import db

from app.models import *

# import jsonify to quickly handle form conversions
from flask import jsonify

# import request to fetch the information about events
from flask import request

import logging

from datetime import datetime
from datetime import timedelta

from flask import render_template

import os

import json
import sonoff

# logger setup
logger = logging.getLogger('my-logger')
logger.propagate = False
logging.basicConfig(filename='event_history.log', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.WARNING)
logging.StreamHandler(stream=None)

s = sonoff.Sonoff("denguner5@gmail.com","smarteff","us")

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
        db.session.commit()
    elif event == 'exit':
        person.is_inside = 0;
        logging.warning('[person_event]A person(id=%s) has left!', str(person_id))
        db.session.commit()


        for device in person.devices:

            # check if there is any suspension for the device
            select_statement = db.select([suspension_request]).where(db.and_(suspension_request.c.person_id==person.person_id, suspension_request.c.device_id==device.device_id))
            query = db.session.execute(select_statement)

            # result
            query = query.first()

            # continue if there is any suspension
            if( query != None):
                continue

            # check if there is any other person assigned to the device
            select_statement = db.select([person_device]).where(person_device.c.device_id==device.device_id)
            query = db.session.execute(select_statement)

            # persons assigned will be listed in this list
            assigned_persons = []
            
            for res in query:
                assigned_persons.append(res.person_id)

            # check if there is any other person is inside
            found = False
            for pers in assigned_persons:
                person2 = Person.query.get_or_404(pers)
                if( person2.is_inside == 1):
                    found = True

            # shutdown will happen in 5 minutes
            shutdown_delay = 300
            date = datetime.now() + timedelta(seconds=shutdown_delay)

            # found==false means that there are no person inside assigned to the device
            if( found == False ):

                # insert scheduled shutdown to table
                scheduled_shutdown = ScheduledShutdown(person.person_id, device.device_id, device.device_name, date)
                db.session.add(scheduled_shutdown)
                db.session.commit()

                token = person.android_token

                # schedule shutdown
                os.system("python3 app/utils/schedule.py " + str(scheduled_shutdown.shutdown_id) + " " + str(device.device_id) + " " + str(shutdown_delay) + "&" )
                
                if (device.device_type == 'Desk' and (token is not None) and person.should_receive_notifications == 1):
                    
                    # notify user
                    os.system("python3 app/notification/notify.py " + str(device.device_id) + " " + str(date) + " " + token + "&")

         
    # prepare the response --> assuming everything is OK
    resp = jsonify({'success':True})

    return resp, 200

# endpoint to handle person events
@app.route("/HandlePersonEventSim", methods=['POST'])
def person_event_sim():

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
        db.session.commit()
    elif event == 'exit':
        person.is_inside = 0;
        logging.warning('[person_event]A person(id=%s) has left!', str(person_id))
        db.session.commit()


        for device in person.devices:

            # check if there is any other person assigned to the device
            select_statement = db.select([person_device]).where(person_device.c.device_id==device.device_id)
            query = db.session.execute(select_statement)

            # persons assigned will be listed in this list
            assigned_persons = []
            
            for res in query:
                assigned_persons.append(res.person_id)

            # check if there is any other person is inside
            found = False
            for pers in assigned_persons:
                person2 = Person.query.get_or_404(pers)
                if( person2.is_inside == 1):
                    found = True

            # shutdown will happen in 15 seconds
            shutdown_delay = 15
            date = datetime.now() + timedelta(seconds=shutdown_delay)

            # found==false means that there are no person inside assigned to the device
            if( found == False ):

                # insert scheduled shutdown to table
                scheduled_shutdown = ScheduledShutdown(person.person_id, device.device_id, device.device_name, date)
                db.session.add(scheduled_shutdown)
                db.session.commit()

                # schedule shutdown
                os.system("python3 app/utils/schedule.py " + str(scheduled_shutdown.shutdown_id) + " " + str(device.device_id) + " " + str(shutdown_delay) + "&" )
                
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

    # get device sonoff id
    device_sonoff_id = device.sonoff_link

    # get device sonoff channel
    device_channel = device.sonoff_channel

    # redirect and log according to action
    if action == 'turnon':

        send_request_device("on", device_sonoff_id, device_channel)

        device.is_on = 1

        db.session.commit()

        logging.warning('[request_event]A person(id=%s) has requested a device(id=%s) to be turned on!', str(person_id), str(device_id))

    elif action == 'turnoff':

        send_request_device("off", device_sonoff_id, device_channel)

        device.is_on = 0

        db.session.commit()

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

    # resolve dates
    now = datetime.now()
    susp_time = datetime(year, month, day, hour, minute, second)

    # resolve suspension in terms of seconds
    diff_time = int((susp_time - now).total_seconds())

    # insert suspension to table
    values = [person_id, device_id, now, susp_time]
    insert_statement = suspension_request.insert().values(values)
    db.session.execute(insert_statement)
    db.session.commit()

    # invoke cleaner
    os.system("python3 app/utils/track_suspension.py " + str(person_id) + " " + str(device_id) + " " + str(diff_time) + "&")    

    logging.warning('[automation_event]A person(id=%s) has requested a suspension for the automation of device(id=%s) until %s!', str(person_id), str(device_id), until)

    # prepare the response --> assuming everything is OK
    resp = jsonify({'success':True})

    return resp, 200


# endpoint to enable automation for a defined person
@app.route("/EnableAutomation", methods=['POST'])
def enable_automation():

    data = request.json
	
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
    
    # remove former enable request
    os.system("python3 app/utils/de_track.py " + str(person_id) + " " + str(device_id))
        
    logging.warning('[automation_event]A person(id=%s) has enabled automation of device(id=%s)', str(person_id), str(device_id))

    # prepare the response --> assuming everything is OK
    resp = jsonify({'success':True})

    return resp, 200

# -----------------------UTILITY ENDPOINTS---------------------------- 
    
# endpoint to clear former shutdown entries
@app.route("/RemoveScheduledShutdown/<sched_id>", methods=['POST'])
def remove_shutdown(sched_id):

    # get scheduled shutdown entry
    scheduled_entry = ScheduledShutdown.query.filter(ScheduledShutdown.shutdown_id==sched_id).first()

    # remove entry
    db.session.delete(scheduled_entry)
    db.session.commit()

    # prepare the response --> assuming everything is OK
    resp = jsonify({'success':True})

    return resp, 200

# endpoint to request suspension of a shutdown
@app.route("/RequestSuspScheduledShutdown/<dev_name>", methods=['POST'])
def request_susp_shutdown(dev_name):

    # get scheduled shutdown entry
    scheduled_entry = ScheduledShutdown.query.filter(ScheduledShutdown.device_name==dev_name).first()

    # terminate background process
    os.system("python3 app/utils/de_schedule.py " + str(scheduled_entry.shutdown_id))
    
    # remove entry
    db.session.delete(scheduled_entry)
    db.session.commit()

    # prepare the response --> assuming everything is OK
    resp = jsonify({'success':True})

    return resp, 200

# endpoint to create new Person
@app.route("/CreateNewPerson/<name>", methods=['GET', 'POST'])
def create_person(name):

    # read new Person's information
    username = name
    is_inside = 0
    should_receive_notifications = 0

    # create Person object
    new_person = Person(person_name=username, is_inside=is_inside, should_receive_notifications = should_receive_notifications)

    # record into DB
    db.session.add(new_person)
    db.session.commit()

    # prepare the response --> assuming everything is OK
    resp = jsonify({'success':True})

    return resp, 200

# endpoint to change assignment of a person-device
@app.route("/ChangeAssignment/<name1>/<name2>", methods=['GET', 'POST'])
def swap_person(name1, name2):

    # fetch persons
    person1 = Person.query.filter(Person.person_name == name1).first()
    person2 = Person.query.filter(Person.person_name == name2).first()

    # devices to be swapped
    devs = person1.devices
    devs2 = person2.devices

    # remove person1's entries
    to_be_deleted = person_device.delete().where(person_device.c.person_id==person1.person_id )
    db.session.execute(to_be_deleted)

    # remove person2's entries
    to_be_deleted = person_device.delete().where(person_device.c.person_id==person2.person_id )
    db.session.execute(to_be_deleted)

    # insert new entries for swapped person
    for dev in devs:
        values = [person2.person_id, dev.device_id]
        insert_statement = person_device.insert().values(values)
        db.session.execute(insert_statement)

    # insert new entries for swapped person
    for dev in devs2:
        values = [person1.person_id, dev.device_id]
        insert_statement = person_device.insert().values(values)
        db.session.execute(insert_statement)

    # record into DB
    db.session.commit()

    # prepare the response --> assuming everything is OK
    resp = jsonify({'success':True})

    return resp, 200

# endpoint to save pre-built event file under server
@app.route("/SaveEvent/<log_name>", methods=['GET', 'POST'])
def save_event(log_name):
    
    data = request.json

    # save file
    with open('app/saved_events/' + str(log_name) + '.json', 'w') as outfile:
        json.dump(data, outfile)

    # prepare the response --> assuming everything is OK
    resp = jsonify({'success':True})

    return resp, 200

# endpoint to request a device turn on/off
@app.route('/turnOperation/<switch_id>/<int:channel>/<turn>')
def sendRequest(turn, switch_id, channel):
    devices = s.get_devices()
    for i in range(len(devices)):
        if devices:
            # We found a device, lets turn something on
            device_id = devices[i]['deviceid']
            if device_id == switch_id:      
                s.switch(turn, switch_id, channel)
    return render_template("ingdog.html", sayfabasligi="SWITCHES",devicelist=devices,deviceid=1)

# endpoint to request a device turn on/off
@app.route('/turnOperation/<switch_id>/<int:channel>/<turn>')
def send_request_device(turn, switch_id, channel):
    devices = s.get_devices()
    print(turn)
    print(switch_id)
    print(channel)
    s.switch(str(turn), str(switch_id), int(channel))

    # prepare the response --> assuming everything is OK
    resp = jsonify({'success':True})

    return resp, 200    
# endpoint to return device status
@app.route('/returnDeviceStatus/<switch_id>')
def device_stats(switch_id):
    array = []  
    counter=0
    counter2=1

    devices = s.get_devices()
    for i in range(len(devices)):
        if devices:
            device_id = devices[i]['deviceid']
            if device_id == switch_id:      
                one=devices[i]['params']['switches'][1]['switch']
                zero=devices[i]['params']['switches'][0]['switch']
                if one == "off":
                    counter=0
                else:
                    counter=1
                if zero == "off":
                    counter2=0
                else:
                    counter2=1
                array.append({"channel-0":counter2,"channel-1":counter})
    return jsonify(array[0])

# return device status from device manager
@app.route('/ReadDeviceStatus')
def read_device_status():
	array = []	
	counter=0
	strike=1
	devices = s.get_devices()
	for i in range(len(devices)):
		if devices:
			device_id = devices[i]['deviceid']
			status=device_id			
			one=devices[i]['params']['switches'][1]['switch']
			zero=devices[i]['params']['switches'][0]['switch']
			if one == "on":
				counter=1
			else:
				counter=0
			if zero == "on":
				strike=1
			else:
				strike=0
		array.append({"id":i,"device_id" : status,"channel_1":one,"channel_0":zero,"channel-0":strike,"channel-1":counter})
	return jsonify(array)


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

# endpoint to list scheduled shutdowns for specified person
@app.route("/ListScheduledShutdowns/<person_id>", methods=['GET'])
def list_scheduled_shutdowns(person_id):

    # get person
    person = Person.query.get_or_404(person_id)

    # scheduled devices waiting to be turned off
    scheduled_devices = ScheduledShutdown.query.filter(ScheduledShutdown.person_id==person_id).all()

    # response json
    shutdown_devices = []

    # append shutdown information as json
    for shutdown in scheduled_devices:
    	shutdown_devices.append(shutdown.serialize)

    # return json
    return jsonify({'scheduledShutdowns': shutdown_devices})

# endpoint to list person-device pairs
@app.route("/ListPersonDeviceAssignment", methods=['GET'])
def list_person_device():

    # get all persons
    persons = Person.query.all()

    # final variable to return
    person_dev_final = {}

    # find personal device of every person
    for person in persons:
        person_dev_final[person.person_name] = ""
        for device in person.devices:
            found = 0
            for person2 in persons:
                for device2 in person2.devices:
                    if (person.person_id == person2.person_id):
                        continue
                    else:
                        if(device2.device_id == device.device_id):
                            found = 1
            if(found == 0):
                tempRes = "D" + str(device.device_id)
                person_dev_final[person.person_name] = tempRes


    # return result as dictionary
    return jsonify(person_dev_final)

# endpoint to list device status
@app.route("/ListDeviceStatus", methods=['GET'])
def list_device_status():

    # get all devices
    devices = Device.query.all()

    device_status = {}

    for device in devices:
        temp_id = "D" + str(device.device_id)
        device_status[temp_id] = device.is_on

    # return result as dictionary
    return jsonify(device_status)


# -----------------------INITIALIZE DB  --------------------------- 

