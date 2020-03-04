from subprocess import PIPE, run
import sys
import os

# --------------USAGE------------------
# $ python3 de_schedule.py <shutDownID> 

# fetch scheduled shutdown ID   
scheduledShutdownID =  int(sys.argv[1])

# returns the terminal output of a given command
def out(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout


# find processes that contain scheduledShutdownID as their cmd-line arg
output = out("ps ax | grep schedule.py\ " + str(scheduledShutdownID))

# split founded processes
lines = output.split("\n")

# create list for the results
found = []

# append matched processes to the list
for line in lines:
    arguments = line.split()
    if (arguments != []):
        if (arguments[2] == 'S'):
            found.append(arguments[0])

# Kill matching scheduled-shutdown processes
for process in found:
    print("Killing:" + str(process))
    command = ( "kill " + str(process) )
    print(command)
    os.system(command)
