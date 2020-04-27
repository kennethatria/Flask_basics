from . import admin
from flask import Blueprint
from flask import render_template, request, url_for, redirect, flash, jsonify, json
from my_app.auth.models import User
from my_app.admin.models import Vehicle, Client, Incident, Service, Feedback
from my_app.auth.forms import EditForm
from my_app.admin.forms import VechileRegistration, ClientDetail, IncidentReport, ServiceForm, CustomerFeedback
from my_app import login_manager, db

admin = Blueprint('admin', __name__)


@admin.route('/', methods=['GET'])
@admin.route('/admin', methods=['GET','POST'])
def home():
    if request.method == 'GET':
        return render_template('admin/index.html')
    elif request.method == 'POST':
        return render_template('admin/index.html')

@admin.route('/vechiles', methods=['GET','POST'])
def vechiles():
    vechilesform = VechileRegistration()
    clientform = ClientDetail()
    vechiles = Vehicle.query.all()
    if request.method == 'POST':
        if vechilesform.validate_on_submit():
            print('Form validation success')
            vechile = Vehicle( client_id = request.form.get(''))
            db.session.add(vechile)
            db.session.commit()
            return render_template('admin/vechiles/index.html',vechiles=vechiles)
        else:
            print(str(request.form.get('client_user')))
            print('Form validation failed !!!')
    else:
        return render_template('admin/vechiles/index.html',vechiles=vechiles,vechilesform=vechilesform, clientform=clientform)

@admin.route('/vechiles-add', methods=['GET','POST'])
def vechile_add():
    vechilesform = VechileRegistration()
    if request.method == 'GET':
        return render_template('admin/vechiles/vechile-add.html',form = vechilesform)
    elif request.method == 'POST':
        if vechilesform.validate_on_submit():
                        print('validation passed')
                        vechile = Vehicle(
                            car_make = vechilesform.car_make.data, 
                            body_type = vechilesform.body_type.data,
                            registration_number = vechilesform.registration_number.data,
                            chassis_number = vechilesform.chassis_number.data,
                            fuel_type = vechilesform.fuel_type.data,
                            year_of_make = vechilesform.year_of_make.data
                        )
                        db.session.add(vechile)
                        db.session.commit()
                        print('data saved')
                        return redirect(url_for('admin.vechiles'))
        else:
            print ('validation failed ')
            if vechilesform.errors:
                flash(vechilesform.errors, 'danger')
                return jsonify({'form validation failed !!!!'})
    else:
        return jsonify({'status':'page unknown'})
    return render_template('admin/vechiles/vechile-add.html',form = vechilesform)

@admin.route('/vechiles-edit/<int:vechile_id>', methods=['GET','POST'])
def vechile_edit(vechile_id):
    print(vechile_id)
    vechile = Vehicle.query.filter_by(id=vechile_id).first_or_404();
    vechilesform = VechileRegistration()
    if request.method == 'POST':
        if vechilesform.validate_on_submit():
            print('validation passed')
            vechile.car_make = vechilesform.car_make.data, 
            vechile.body_type = vechilesform.body_type.data,
            vechile.registration_number = vechilesform.registration_number.data,
            vechile.chassis_number = vechilesform.chassis_number.data,
            vechile.fuel_type = vechilesform.fuel_type.data,
            vechile.year_of_make = vechilesform.year_of_make.data,
            db.session.commit()
            flash('Edit Saved')
            return redirect(url_for('admin.vechile_info',vechile=vechile_id))
        else:
            print('validation failed')
    elif request.method == 'GET':
        return render_template('admin/vechiles/vechile-edit.html',form=vechilesform, vechile=vechile)
    else: 
        return jsonify({'status':'request not specifited'})

@admin.route('/vechile-info/<int:vechile>')
def vechile_info(vechile):
    vechile = Vehicle.query.filter_by(id=vechile).first_or_404();
    return render_template('admin/vechiles/vechile-info.html',vechile=vechile)

@admin.route('/clients', methods=['GET','POST'])
def clients():
    clients = Client.query.all()
    return render_template('admin/clients/index.html', clients = clients)
    

@admin.route('/client-add', methods=['GET','POST'])
def client_add():
    clientform = ClientDetail()
    if request.method == 'GET':
        return render_template('admin/clients/client-add.html',form = clientform )
    elif request.method == 'POST':
        if clientform.validate_on_submit():
            print('validation passed !!!')
            client = Client( 
                username = clientform.username.data,
                email = clientform.email.data,
                telephone = clientform.telephone.data,
                telephone_alternative = clientform.telephone_alternative.data,
                location = clientform.location.data,
                dob = clientform.dob.data,
                occupation = clientform.occupation.data,
                place_of_work = clientform.place_of_work.data
            )
            db.session.add(client)
            db.session.commit()
            return redirect(url_for('admin.clients'))
        else: 
            print('validation failed !!!')
            if clientform.errors:
                flash(clientform.errors, 'danger') 
                return redirect(url_for('admin.clients'))

@admin.route('/client-info/<int:client_id>')
def client_info(client_id):
    client = Client.query.filter_by(id=client_id).first_or_404()
    return render_template('admin/clients/client-info.html', client=client)

@admin.route('/client-edit/<int:client_id>', methods=['POST','GET'])
def client_edit(client_id):
    client = Client.query.filter_by(id=client_id).first_or_404();
    clientform = ClientDetail()
    if request.method == 'POST':
        if clientform.validate_on_submit():
            client.username = clientform.username.data
            client.email = clientform.email.data
            client.telephone = clientform.telephone.data
            client.telephone_alternative = clientform.telephone_alternative.data,
            client.location = clientform.location.data,
            client.dob = clientform.dob.data,
            client.occupation = clientform.occupation.data,
            client.place_of_work = clientform.place_of_work.data
            db.session.commit()
            return redirect(url_for('admin.client_info',client_id=client_id))
        else:
            print('validation failed')
            return redirect(url_for('admin.clients'))
    elif request.method == 'GET':
        return render_template('admin/clients/client-edit.html',form=clientform, client = client )
    else: 
        return jsonify({'status':'request not specifited'})

@admin.route('/users')
def users():
    editform = EditForm()
    users = User.query.all()
    return render_template('admin/users.html', users=users, editform=editform)

@admin.route('/feedback')
def feedback():
    feedbacks = Feedback.query.all()
    return render_template('admin/feedback/feedback-index.html', feedbacks = feedbacks)

@admin.route('/feedback-add', methods=['GET','POST'])
def feedback_add():
    form = CustomerFeedback()
    if request.method == 'POST':
        if form.validate_on_submit():
            feedback = Feedback( user_id = form.user.data, rating = form.rating.data, service_id = form.service_id.data, location = form.location.data)
            db.session.add(feedback)
            db.session.commit()
            return redirect(url_for('admin.feedback'))
        else: 
            if form.errors:
                flash(form.errors, 'danger')
                return redirect(url_for('admin.feedback'))
    elif request.method == 'GET':
        return render_template('admin/feedback/feedback-add.html', form = form)

@admin.route('/feedback-edit/<int:feedback_id>', methods=['POST','GET'])
def feedback_edit(feedback_id):
    form = CustomerFeedback()
    feedback = Feedback.query.filter_by(id = feedback_id).first_or_404()
    feedback = Feedback( user_id = form.user.data, rating = form.rating.data, service_id = form.service_id.data, location = form.location.data)
    db.session.commit()
    return render_template('admin/feedback/feedback-edit.html', feedback = feedback)

@admin.route('/feedback-info/<int:feedback_id>', methods=['POST','GET'])
def feedback_info(feedback_id):
    feedbacks = Feedback.query.filter_by(id = feedback_id).first_or_404()
    return render_template('admin/feedback/feedback-info.html', feedbacks = feedbacks)

@admin.route('/incidents')
def incidents():
    incidents = Incident.query.all()
    return render_template('admin/incidents/index.html', incidents = incidents)

@admin.route('/incident-add', methods = ['POST','GET'])
def incident_add():
    form = IncidentReport()
    if request.method == 'GET':
        return render_template('admin/incidents/add.html', form = IncidentReport())
    if request.method == 'POST':
        if form.validate_on_submit():
            incident = Incident( membership_number = form.membership_number.data, location = form.location.data, defect = form.defect.data , photo_name = form.photo_name.data )
            db.session.add(incident)
            db.session.commit()
            return redirect(url_for('admin.incidents'))
        else: 
            if form.errors:
                flash(form.errors, 'danger') 
                return redirect(url_for('admin.incidents'))
    else: 
        return jsonify({'status':'not allowed !!!'})

@admin.route('/incident-edit/<int:incident_id>', methods = ['POST','GET'])
def incident_edit(incident_id):
    form = IncidentReport()
    incident = Incident.query.filter_by(id = incident_id).first_or_404()
    if request.method == 'GET':
        return render_template('admin/incidents/edit.html', form = IncidentReport(), incident = incident)
    if request.method == 'POST':
        if form.validate_on_submit():
            incident = Incident( membership_number = form.membership_number.data, location = form.location.data, defect = form.defect.data , photo_name = form.photo_name.data )
            db.session.commit()
            return redirect(url_for('admin.incidents'))
        else: 
            if form.errors:
                flash(form.errors, 'danger') 
                return redirect(url_for('admin.incidents'))
    else: 
        return jsonify({'status':'not allowed !!!'})

@admin.route('/incident-info/<int:incident_id>')
def incident_info(incident_id):
    incident = Incident.query.filter_by(id = incident_id).first_or_404()
    if request.method == 'GET':
        return render_template('admin/incidents/info.html', incident = incident)
    else: 
        return jsonify({'status':'not allowed !!!'})

@admin.route('/service')
def services():
    services = Service.query.all()
    return render_template('admin/services/service-index.html', services = services)

@admin.route('/service-edit/<int:service_id>', methods=['GET','POST'])
def service_edit(service_id):
    form = ServiceForm()
    service = Service.query.filter_by(id = service_id).first_or_404()
    if request.method == 'GET':
        return render_template('admin/services/service-edit.html', form = form, service = service )
    elif request.method == 'POST':
        if form.validate_on_submit():
            service.name = form.name.data,
            service.location = form.location.data,
            service.contact = form.contact.data,
            service.service_type = form.service_type.data ,
            service.service_photo = form.service_photo.data,
            service.operating_time = form.operating_time.data,
            service.service_struture = form.service_structure.data,
            service.account_manager = form.account_manager.data
            db.session.commit()
            return redirect(url_for('admin.services'))
        elif form.errors:
            flash(form.errors, 'danger')
            return redirect(url_for('admin.services'))
        else: 
            return jsonify({'message':'something went wrong !!!'})
    

@admin.route('/service-add', methods = ['POST','GET'])
def service_add():
    form = ServiceForm()
    if request.method == 'GET':
        return render_template('admin/services/service-add.html', form = ServiceForm())
    if request.method == 'POST':
        if form.validate_on_submit():
            service = Service(
                name = form.name.data,
                location = form.location.data,
                contact = form.contact.data,
                service_type = form.service_type.data ,
                service_photo = form.service_photo.data,
                operating_time = form.operating_time.data,
                service_structure = form.service_structure.data,
                account_manager = form.account_manager.data
            )
            db.session.add(service)
            db.session.commit()
            return redirect(url_for('admin.services'))
        else: 
            if form.errors:
                flash(form.errors, 'danger') 
                return redirect(url_for('admin.service'))
    else: 
        return jsonify({'status':'not allowed !!!'})

@admin.route('/service-info/<int:service_id>')
def service_info(service_id):
    service = Service.query.filter_by(id = service_id).first_or_404()
    if request.method == 'GET':
        return render_template('admin/services/service-info.html', service = service)
    else: 
        return jsonify({'status':'not allowed !!!'})

@admin.route('/posts/', methods=['POST','GET'])
def posts():
    if request.method == 'POST':
        if request.data is None:
            return jsonify({'status':'no action !!!'})
        else:
            if request.form.get('action') == 'user-details':
                users = User.query.all()
                users_obj = []
                for user in users:
                    users_obj.append({
                        'username' : user.username,
                        'company' : user.company,
                        'email' : user.email,
                        'gender' : user.gender
                    });
                return jsonify({'user':users_obj});
            elif request.headers['Content-Type'] == 'application/json':
                return jsonify({'status':'kenneth'})
            else:    
                return jsonify(request.form.get('action'))
    elif request.method == 'GET':
        return jsonify({'message':'hello world !!!'});

@admin.route('/api/', methods=['POST','GET'])
def api():
    if request.method == 'POST':
        if request.data is not None:
            data = json.loads(request.data)
            if data['action'] == 'verify_user':
                userId = verifyUser(data['username'])
                return jsonify({
                        'status':'ok',
                        'user_id': userId
                })
            elif data['action'] == 'incident_registration':
                response = incident_registration(request.data)
                print(response)
                if response is not None:
                    return jsonify({"message":"success"})
                else:
                    return jsonify(response)
            else:
                return jsonify({'message':'action not allowed !!!'})
        else:
            return jsonify({'status':'error'})
    elif request.method == 'GET':
        return jsonify({'status':'success','message':'get response !!!!'})

def incident_registration(incident_obj):
    if incident_obj is not None:
        data = json.loads(incident_obj)
        if data['action'] == 'incident_registration':
            incident = Incident(
                vechile_registration_number = data['vechile_registration'],
                contact_number = data['contact'],
                incident_location = data['location']
            )
            db.session.add(incident)
            db.session.commit()
            return "ok"
        else:
            return 'error'

def verifyUser(user_name):
    print('here')
    user = User.query.filter_by(username = str(user_name)).first_or_404()
    if user is not None:    
        return user.id
    else:
        return 'false'
    
    