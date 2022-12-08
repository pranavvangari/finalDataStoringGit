from . import db

class Name(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(100))
    temp_id = db.Column(db.Integer)
    

def displayNames(currentArr):
    namesModel = []
    for x in currentArr:
        namesModel.append(currentArr[x])
    
    return namesModel


    
    



   
   


    
    