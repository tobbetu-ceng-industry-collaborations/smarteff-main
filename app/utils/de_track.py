from subprocess import PIPE, run
import sys
import os

# --------------USAGE------------------
# $ python3 de_track.py <person_id> <device_id> 

# fetch person and device ID   
person_id = int(sys.argv[1])
device_id = int(sys.argv[2])

# returns the terminal output of a given command
def out(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout


# find processes that contain personID and deviceID as their cmd-line arg
output = out("ps ax | grep track_suspension.py\ " + str(person_id) + "\ " + str(device_id))

# split founded processes
lines = output.split("\n")

# create list for the results
found = []

# append matched processes to the list
for line in lines:
    arguments = line.split()
    if (arguments != []):
        if (arguments[2] == 'S' or arguments[2] == 'S+'):
            found.append(arguments[0])

# Kill matching suspension track processes
for process in found:
    print("Killing:" + str(process))
    command = ( "kill " + str(process) )
    print(command)
    os.system(command)
