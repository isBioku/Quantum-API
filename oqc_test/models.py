import string
from oqc_test.application import db
from datetime import datetime


class OqcModel(db.Model):
    id = db.Column (db.Integer, primary_key = True)
    input_string = db.Column(db.String(100))
    result = db.Column(db.String(100))
    date = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __init__(self, input_string, result) :
        self.input_string = input_string
        self.result = result
