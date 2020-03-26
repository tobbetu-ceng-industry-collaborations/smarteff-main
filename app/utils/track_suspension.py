import sched, time
import sys
import os

# RUN THIS SCRIPT AS:
# $ python3 track_suspension.py <person_id> <device_id> <secondsUntilSuspensionHalts>&

# create scheduler
s = sched.scheduler(time.time, time.sleep)

# turn device off with its given id
def track_susp(dev_id, person_id):

	# make call from test_api
	os.system(("bash test_api/Heroku/POST/enable_automation.sh " +  str(dev_id) + " " + str(person_id)).format())

# general scheduler
def schedule(device_id, person_id, until_suspension):

    # enter queue
    s.enter(until_suspension, 1, track_susp, argument=(device_id, person_id,))
    
    # execute queue
    s.run()

# fetch device ID  
deviceID =  int(sys.argv[2])

# fetch suspension time in terms of seconds  
until_suspension =  int(sys.argv[3])

# fetch person id
person_id = int(sys.argv[1])

# schedule shutdown event
schedule(deviceID, person_id, until_suspension)
