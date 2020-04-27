
from my_app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    car_make  = db.Column(db.String())
    body_type = db.Column(db.String())
    registration_number = db.Column(db.String())
    chassis_number = db.Column(db.String())
    fuel_type = db.Column(db.String())
    year_of_make = db.Column(db.String())
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    email = db.Column(db.String())
    telephone = db.Column(db.String())
    telephone_alternative = db.Column(db.String())
    location = db.Column(db.String())
    dob = db.Column(db.String())
    occupation = db.Column(db.String())
    place_of_work =db.Column(db.String())
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
        
    def __repr__(self):
        return '<Client {} >'.format(self.id)

class Incident(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    car_make = db.Column(db.String())
    vechile_registration_number = db.Column(db.String())
    contact_number = db.Column(db.String())
    incident_location = db.Column(db.String())
    photo_one = db.Column(db.String())
    photo_two = db.Column(db.String())
    photo_three = db.Column(db.String())
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    location = db.Column(db.String())
    contact = db.Column(db.String())
    service_type = db.Column(db.String())
    service_structure = db.Column(db.String())
    service_photo = db.Column(db.String())
    operating_time = db.Column(db.String())
    account_manager = db.Column(db.String())
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String())
    rating = db.Column(db.String())
    service_id = db.Column(db.String())
    location = db.Column(db.String())
    issue = db.Column(db.String())



