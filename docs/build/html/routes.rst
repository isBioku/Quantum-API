This is file that handles the url of the system. 
It communicates with the form class to request for the actions of the user 

This file also contains the checker function, which only takes in viable job from the user. 
this function reads the patter of the job input by the user, and uses the re (regular expression) module was used to check the pattern of the job input
If the pattern matches, it passes it to the instance of the runtime class  for it to be processed by the execute function.


Also in this file is the history function which queries the databse for the list of successful jobs execution


from flask import render_template, flash, request
from oqc_test import app
from oqc_test.input_form import InputForm
from oqc_test.runtime import Runtime
import re
import asyncio
from oqc_test.models import OqcModel

class Main :
    @app.route("/")
    @app.route("/home")
    def home():
        form = InputForm()
        return render_template("index.html", title='Home', form = form)


    @app.route("/checker", methods = ["POST", "GET"])
    def checker():
        form = InputForm()
        if form.validate_on_submit():
            try:
                input_string = form.inputString.data
                pattern =re.compile(r"[a-zA-Z]\(\d\d\)\,\s[a-zA-Z]\(\d\d\d\)\,\s[a-zA-Z]\(\d\d\)")
                if pattern.match(input_string):            
                    runtime = Runtime()
                    asyncio.run(runtime.execute(input_string))
                else:
                    flash(f'Execution Failed, The pattern of the string does not match', 'danger')
            except Exception:
                flash(f'Field cannot be Empty', 'danger')         
        
        return render_template("index.html", title='Home', form = form)  
        
    @app.route("/get_history", methods = ['POST', "GET"])
    def get_history():
        form = InputForm()
        if request.method == 'GET':
            list_of_history = OqcModel.query.all()
            return render_template("index.html", form=form, histories = list_of_history)


    
    

       
          

