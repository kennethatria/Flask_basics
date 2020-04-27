from my_app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    location = db.Column(db.String(255))
    company = db.Column(db.String(255))
    gender = db.Column(db.String(255))
    photo_dir = db.Column(db.String(255))
    password_hash= db.Column(db.String(255))

    '''
    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return unicode(self.id)

    '''
    
    def set_password(self, user_password):
        self.password_hash = generate_password_hash(user_password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User: {}>'.format(self.username)
    
    # Set up user_loader
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

class Permissions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    admin = db.Column(db.Boolean())
    client = db.Column(db.Boolean())
    service_provider = db.Column(db.Boolean())
    root = db.Column(db.Boolean())

