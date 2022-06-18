from flask import render_template, flash, request
from oqc_test import application
from oqc_test.input_form import InputForm
from oqc_test.runtime import Runtime
import re
import asyncio
from oqc_test.models import OqcModel


    
class Main :
    @application.route("/")
    @application.route("/home")
    def home():
        form = InputForm()
        return render_template("index.html", title='Home', form = form)


    @application.route("/checker", methods = ["POST", "GET"])
    def checker():
        form = InputForm()
        if form.validate_on_submit():
            try:
                input_string = form.inputString.data
                pattern =re.compile(r"X\(\d+\)\,\sY\(\d+\)\,\sZ\(\d+\)")
                if pattern.match(input_string):            
                    runtime = Runtime()
                    asyncio.run(runtime.execute(input_string))
                else:
                    flash(f'Execution Failed, The pattern of the string does not match', 'danger')
            except Exception:
                flash(f'Field cannot be Empty', 'danger')         
        
        return render_template("index.html", title='Home', form = form)  
        
    @application.route("/get_history", methods = ['POST', "GET"])
    def get_history():
        form = InputForm()
        if request.method == 'GET':
            list_of_history = OqcModel.query.all()
            return render_template("index.html", form=form, histories = list_of_history)


    
    

       
          

