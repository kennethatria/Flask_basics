from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager
from config import app_config

app = Flask(__name__)
app.config.from_object(app_config['development'])

login_manager = LoginManager()
db = SQLAlchemy(app)

#from my_app.admin.models import Vehicle
from my_app.auth.models import User, Permissions

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

login_manager.init_app(app)
login_manager.login_view = 'login'

from my_app.auth.views import auth
app.register_blueprint(auth)
from my_app.admin.views import admin
app.register_blueprint(admin)