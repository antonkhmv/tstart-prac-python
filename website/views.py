from flask import Blueprint, render_template
from flask import request, flash, jsonify
from flask_login.utils import login_required
from flask_login import current_user 
from . import db
import json 

views = Blueprint('views', __name__)

@views.route('/work')
@login_required
def work():
    return "<h1> lol </h1>"

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():

    # if request.method == 'POST':
    #     data = request.form.get('')

    return render_template("home.html", user=current_user)
