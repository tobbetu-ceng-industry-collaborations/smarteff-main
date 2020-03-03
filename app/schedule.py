import sched, time
import sys
import os

# RUN THIS SCRIPT AS:
# $ nohup python3 schedule.py <Scheduled Shutdown ID> &
# $ ps ax | grep schedule.py -> will return processes called from this script
# you can kill the processes with matching Scheduled shutdown ID before autonomous shutdown happens 

# create scheduler
s = sched.scheduler(time.time, time.sleep)

# request a device to be turned off with its given id
def request_device_off(dev_id):
	os.system(("bash ../test_api/POST/request_device_off.sh " +  str(dev_id)).format())

# turn device off with its given id
def device_off(dev_id):
	
	# print(("bash ../test_api/POST/device_off.sh " +  str(dev_id)).format())
	
	# make call from test_api
	os.system(("bash ../test_api/POST/device_off.sh " +  str(dev_id)).format() )

# general scheduler
def schedule():

	#temp device id, dont forget to read real device id from table..
    device_id = 2

    # enter queue
    s.enter(3, 1, device_off, argument=(device_id,))
    
    #execute queue
    s.run()

# fetch scheduled shutdown ID   
scheduledShutdownID =  int(sys.argv[1])

# dont forget to fetch deviceID-personIO from tables.
# you will referencing a scheduled shutdown with the IDs given..
schedule()