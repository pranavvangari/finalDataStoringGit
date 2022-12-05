from flask import Blueprint, flash, render_template, request
from .models import Name, Temp
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    name = request.form.get('name') 
    if request.method == 'POST':
        #name = request.form.get('name') 
        if len(name) > 1:
            new_name = Name(data=name)
            db.session.add(new_name)
            db.session.commit() 
            flash('Saved', category='success')

        else:

            flash('Not saved', category='error')



    return render_template("home.html", namesToDisplay=Temp()) 



@views.route('/input', methods=['GET', 'POST'])
def input():

    return render_template("input.html")