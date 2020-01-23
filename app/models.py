# Import the database object from the main app module
from app import db

# Define person model
class Person(db.Model):
    person_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    person_name = db.Column(db.String(128),nullable=False)
    is_inside = db.Column(db.Boolean, nullable=False)
    should_receive_notifications = db.Column(db.Boolean,nullable=False)
    
    def __init__(self, person_name, is_inside, should_receive_notifications):
        self.person_name = person_name
        self.is_inside = is_inside
        self.should_receive_notifications = should_receive_notifications


