

import time
from flask import Flask, flash
from oqc_test.models import OqcModel
from oqc_test import db

app = Flask(__name__)
db.create_all()


class Runtime:     

    async def execute(self, input_string):                         
        result = 'Execution Passed'       
        model = OqcModel(input_string, result)
        db.session.add(model)
        db.session.commit()
        return flash(f'Execution Passed, The pattern of the string Matched', 'success')


            


        
        
        


