from flask import Blueprint, flash, render_template, request, session
from .models import Name
from . import db

views = Blueprint('views', __name__)

tempName = None
specificArr = ["red", "blue"]


@views.route('/', methods=['GET', 'POST'])
def home():
    
    name = request.form.get('name')
    
    if request.method == 'POST':
        
        if len(name) > 1:
            new_name = Name(data=name)
            specificArr.append(name)
            db.session.add(new_name)
            db.session.commit()
            print(specificArr)
            flash('Saved', category='success')

        else:

            flash('Not saved', category='error')
    

    return render_template("home.html", namesToDisplay=Name.query.all()) 


outputArr = ["ben", "pranav"]
@views.route('/input', methods=['GET', 'POST'])
def input():

    name = request.form.get('name')

    if request.method == 'POST':
        
        for x in specificArr:
            if x == name:
                outputArr.append(x)

        





    return render_template("input.html", namesToDisplay=Name.query.all(), arr=specificArr, name=name, filteredArr=outputArr)