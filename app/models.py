# Import the database object from the main app module
from app import db

# person_device table to keep track of the relation between persons and devices
person_device = db.Table('person_device',
    db.Column('person_id', db.Integer, db.ForeignKey('Person.person_id')),
    db.Column('device_id', db.Integer, db.ForeignKey('Device.device_id'))
    )

# person_device table to keep track of the relation between persons and devices
suspension_request = db.Table('suspension_request',
    db.Column('person_id', db.Integer, db.ForeignKey('Person.person_id')),
    db.Column('device_id', db.Integer, db.ForeignKey('Device.device_id')),
    db.Column('suspension_start', db.DateTime, nullable=False),
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


