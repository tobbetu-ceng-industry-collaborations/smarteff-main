import sched, time
import sys
import os

# RUN THIS SCRIPT AS:
# $ python3 schedule.py <Scheduled Shutdown ID> <Device ID> <secondsUntilShutdown>&

# create scheduler
s = sched.scheduler(time.time, time.sleep)

# request a device to be turned off with its given id
def request_device_off(dev_id):
	os.system(("bash test_api/Heroku/POST/request_device_off.sh " + "1" + " " + str(dev_id)).format())

# turn device off with its given id
def device_off(dev_id, shut_id):

	# make call from test_api - turn device off from device manager
	request_device_off(dev_id)

	# make call from test_api - change device status as turned off
	os.system(("bash test_api/Heroku/POST/device_off.sh " +  str(dev_id)).format())

	# make call from test_api - remove shutdown entry
	os.system(("bash test_api/Heroku/POST/remove_shutdown.sh " +  str(shut_id)).format())

# general scheduler
def schedule(device_id, until_suspension, shut_id):

    # enter queue
    s.enter(until_suspension, 1, device_off, argument=(device_id, shut_id,))
    
    # execute queue
    s.run()

# fetch scheduled shutdown ID   
scheduledShutdownID =  int(sys.argv[1])

# fetch device ID  
deviceID =  int(sys.argv[2])

# fetch suspension time in terms of seconds  
until_suspension =  int(sys.argv[3])

# schedule shutdown event
schedule(deviceID, until_suspension, scheduledShutdownID)
