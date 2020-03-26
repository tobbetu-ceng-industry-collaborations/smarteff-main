from __future__ import print_function
import datetime
import firebase_admin
from firebase_admin import messaging
from firebase_admin import credentials

import sys

def send_to_token():

    # Tests user's token
    registration_token = "cZvz6ae1XBM:APA91bFd0ReIxpz281IRDCL7pYdFZdx_0SQF6_dYfm13OgnE-f6hIlwh2FlKtu2F2170BVBlDJMsRmworTzZJQ4wP-YQo9_R10cI9swZtFFLf5l-8scj4nqpD1XIUXW91U9bGzK3xec6"

    # Prepare message
    message = messaging.Message(
        data={
            'device_id': '850',
            'date': '2:45',
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

device_id = str(sys.argv[1])
date = str(sys.argv[2])
send_to_token()