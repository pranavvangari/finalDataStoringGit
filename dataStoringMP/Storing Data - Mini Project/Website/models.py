from . import db

class Name(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(100))
    temp_id = db.Column(db.Integer, db.ForeignKey('temp.id'))


class Temp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    allNames = db.relationship('Name')   
   


    
    