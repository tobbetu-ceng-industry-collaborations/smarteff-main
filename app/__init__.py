from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask import Flask, request, render_template

app = Flask(__name__)
CORS(app)

# Configurations
app.config.from_object('config')

# Define the database object
db = SQLAlchemy(app)

from app import views
from app import models
from app import controllers

# from app.models import *

# import sonoff

# s = sonoff.Sonoff("denguner5@gmail.com","smarteff","us")
# array = []	
# counter=0
# strike=1
# devices = s.get_devices()
# for i in range(len(devices)):
# 	if devices:
# 		device_id = devices[i]['deviceid']
# 		status=device_id			
# 		one=devices[i]['params']['switches'][1]['switch']
# 		zero=devices[i]['params']['switches'][0]['switch']
# 		if one == "on":
# 			counter=1
# 		else:
# 			counter=0
# 		if zero == "on":
# 			strike=1
# 		else:
# 			strike=0
# 	array.append({"id":i,"device_id" : status,"channel_1":one,"channel_0":zero,"channel-0":strike,"channel-1":counter})

# for elem in array:
# 	device = Device.query.filter(Device.sonoff_link == elem['device_id'], Device.sonoff_channel == 0).first()
# 	device1 = Device.query.filter(Device.sonoff_link == elem['device_id'], Device.sonoff_channel == 1).first()
# 	device.is_on = int(elem['channel-0'])
# 	device1.is_on = int(elem['channel-1'])
# 	db.session.commit()