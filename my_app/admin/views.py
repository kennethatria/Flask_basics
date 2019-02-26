from . import admin
from flask import Blueprint
from flask import render_template, request
#from my_app.auth.models import MESSAGES

admin = Blueprint('admin', __name__)

@admin.route('/admin')
def home():
    return render_template('admin/index.html')