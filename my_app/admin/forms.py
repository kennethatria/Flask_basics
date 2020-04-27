# app/admin/forms.py
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError, SelectField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms.widgets import TextArea


class VechileRegistration(FlaskForm):
    car_make = StringField('Car Make', validators=[DataRequired()])
    body_type =  StringField('Body Type', validators=[DataRequired()])
    registration_number =  StringField('Registration Number')
    chassis_number =  StringField('Chassis Number')
    fuel_type =  SelectField('Fuel', choices=[('Petrol','Petrol'),('Diseal','Diseal')],validators=[DataRequired()])
    year_of_make =  StringField('Year of Make')

class ClientDetail(FlaskForm):
    username =  StringField('Name')
    email =  StringField('Email')
    telephone =  StringField('Telephone')
    telephone_alternative =  StringField('Alternative Telephone')
    location = StringField('Address')
    dob = StringField('DOB')
    occupation = StringField('Occupation')
    place_of_work = StringField('Place of Work')

class ServiceForm(FlaskForm):
    name = StringField('Service Provider Name', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])   
    contact = StringField('Contact') 
    service_type = SelectField('Service Type', choices=[('engine','Engine'),('tyres','Tyres'),('all','All')])
    service_photo = StringField('Photo')
    operating_time = SelectField('Work Hours', choices=[('day','Day'),('Night','Night'),('Full Time','Full Time')])
    service_structure = SelectField('Service Structure', choices=[('personal','Personal'),('Company','Company')])
    account_manager = StringField('Account Contact')
    

class IncidentReport(FlaskForm):
    membership_number = StringField('Membership Number')
    location = StringField('Location')
    defect = SelectField('Select Incident', choices=[('fuel','Fuel'),('battery','Battery'),('tire','Tire'),('other','Other')])
    photo_name = StringField('Photo')

class CustomerFeedback(FlaskForm):
    user = StringField('User')
    rating = SelectField('Rating', choices=[('good','Good'),('average','Average'),('low','Low')])
    service_id = StringField('Service Provider')
    location = StringField('location')
    issue = StringField('Issue', widget=TextArea())


    


