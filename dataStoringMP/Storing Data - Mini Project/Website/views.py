from flask import Blueprint, flash, render_template, request, session
from .models import Name
from . import db

views = Blueprint('views', __name__)

tempName = None






@views.route('/', methods=['GET', 'POST'])
def home():
    
    name = request.form.get('name')
    
    if request.method == 'POST':
        
        if len(name) > 1:
            new_name = Name(data=name)
            db.session.add(new_name)
            db.session.commit()
            
            flash('Saved', category='success')

        else:

            flash('Not saved', category='error')

        
        
    

    return render_template("home.html", namesToDisplay=Name.query.all()) 





@views.route('/input', methods=['GET', 'POST'])
def input():

    
    outputArr = ["ben", "pranav"]
    databaseArr = ["red", "blue"]
    

    if request.method == 'POST':
        name = request.form.get("findName")

        
        tempArr = Name.query.all()
        outputArr = ["ben", "pranav", "yehan"]
        for x in tempArr:
            databaseArr.append(x.data)

        
        for y in databaseArr:
            if name == y:
                outputArr.append(y)
        
            



    return render_template("input.html", namesToDisplay=Name.query.all(), databaseArr=databaseArr, name=name, outputArr=outputArr)
