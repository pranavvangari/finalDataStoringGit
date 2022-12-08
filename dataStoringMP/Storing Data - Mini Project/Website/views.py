from flask import Blueprint, flash, render_template, request
from .models import Name, displayNames
from . import db

views = Blueprint('views', __name__)

namesArr = ["josh", "pranav"]
#namesArr.append(Name.query.filter_by(data=Name.data).all())

@views.route('/', methods=['GET', 'POST'])
def home():
    name = request.form.get('name')
    
    

    if request.method == 'POST':
        
        print(namesArr)
        
        if len(name) > 1:
            new_name = Name(data=name)
            
            db.session.add(new_name)
            db.session.commit() 
            #namesArr.append(new_name.data)
            #displayNames(namesArr)
            print("namesArr")
            flash('Saved', category='success')

        else:

            flash('Not saved', category='error')
    

    return render_template("home.html", namesToDisplay=Name.query.all()) 



@views.route('/input', methods=['GET', 'POST'])
def input():

    return render_template("input.html")