from __future__ import print_function
import datetime
import firebase_admin
from firebase_admin import messaging
from firebase_admin import credentials

import sys

def send_to_token(device_id, date, token):

    # Tests user's token
    registration_token = token

    # Prepare message
    message = messaging.Message(
        data={
            'device_id': device_id,
            'date': date,
        },
        token=registration_token,
    )

    # Send a message to the device corresponding to the provided
    # registration token.
    response = messaging.send(message)
    # Response is a message ID string.
    print('Successfully sent message:', response)
    # [END send_to_token]

cred = credentials.Certificate("app/notification/smarteff-e4fef-firebase-adminsdk-3y2fw-b0a6f2de74_1.json")
firebase_admin.initialize_app(cred)

# read data from cmd args
device_id = str(sys.argv[1])
date = str(sys.argv[3])
token = str(sys.argv[4])
date = date[0:8]

print(token)

send_to_token(device_id, date, token)
exit()