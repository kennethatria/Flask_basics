from flask import render_template, request, url_for, redirect, flash
from flask_login import current_user, login_user, logout_user, login_required
from my_app import login_manager, db
from forms import LoginForm, RegistrationForm
from .import auth
from my_app.auth.models import User

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'GET':
        return render_template('auth/registration.html',form=form)
    elif request.method == 'POST':
        if form.validate_on_submit():
            user = User(email= form.email.data, username = form.username.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        else:
            if form.errors:
                flash(form.errors, 'danger') 
        return render_template('auth/registration.html',form=form)      

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(url_for('admin.home'))
        else:
            flash('Invalid Username or Password !!!')
    else:
        if form.errors:
            flash(form.errors, 'danger') 
    return render_template('auth/login.html',form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have successfully been logged out.')
    return redirect(url_for('auth.login'))
