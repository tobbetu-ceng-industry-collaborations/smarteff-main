# Import the database object from the main app module
from app import db

from datetime import datetime

# person_device table to keep track of the relation between persons and devices
person_device = db.Table('person_device',
    db.Column('person_id', db.Integer, db.ForeignKey('Person.person_id')),
    db.Column('device_id', db.Integer, db.ForeignKey('Device.device_id'))
    )

# suspension_request table to keep track of the suspensions of devices
suspension_request = db.Table('suspension_request',
    db.Column('person_id', db.Integer, db.ForeignKey('Person.person_id')),
    db.Column('device_id', db.Integer, db.ForeignKey('Device.device_id')),
    db.Column('suspension_start', db.DateTime, nullable=False, default=datetime.utcnow),
    db.Column('suspension_end', db.DateTime, nullable=False),
    )

# Define person model
class Person(db.Model):

    __tablename__ = 'Person'

    person_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    person_name = db.Column(db.String(128),nullable=False)
    is_inside = db.Column(db.Integer, nullable=False)
    should_receive_notifications = db.Column(db.Integer,nullable=False)

    devices = db.relationship('Device', secondary=person_device, backref=db.backref('assigned_persons', lazy='dynamic'))
    
    def __init__(self, person_name, is_inside, should_receive_notifications):
        self.person_name = person_name
        self.is_inside = is_inside
        self.should_receive_notifications = should_receive_notifications

   # Serialize json object
    @property
    def serialize(self):
        return {'id':self.person_id,'name': self.person_name}

# Define device model
class Device(db.Model):

    __tablename__ = 'Device'

    device_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    device_name = db.Column(db.String(128),nullable=False)
    is_on = db.Column(db.Integer, nullable=False)

    suspensions = db.relationship('Person', secondary=suspension_request, backref=db.backref('suspension_requests', lazy='dynamic'))
        
    def __init__(self, device_name, is_on):
        self.device_name = device_name
        self.is_on = is_on

   # Serialize json object
    @property
    def serialize(self):
        return {'id':self.device_id,'name':self.device_name,'isOn':self.is_on,'automation':''}

# Define scheduled shutdown model
class ScheduledShutdown(db.Model):

    __tablename__ = 'scheduled_shutdown'

    shutdown_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    person_id = db.Column(db.Integer, nullable=False)
    device_id = db.Column(db.Integer, nullable=False)
    device_name = db.Column(db.String(128),nullable=False)
    shutdown_time = db.Column(db.DateTime, nullable=False)

    def __init__(self, person_id, device_id, device_name, shutdown_time):
        self.person_id = person_id
        self.device_id = device_id
        self.device_name = device_name
        self.shutdown_time = shutdown_time

   # Serialize json object
    @property
    def serialize(self):
        return {'device':{'id':self.device_id,'name':self.device_name},'timestamp':self.shutdown_time}


