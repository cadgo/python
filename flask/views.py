from flask import Blueprint, render_template, redirect
from .models import DATABASE
import os
views = Blueprint('views', __name__)

@views.route('/')
def mainpage():
    if os.path.isfile(DATABASE):
        return redirect('databasecreate')
    else:
        print(DATABASE)
    return render_template('base.html')

@views.route('/databasecreate', methods=['GET'])
def databasecreate():
    return '<h1>database creation</h1>'
