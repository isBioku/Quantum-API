This file uses the wtforms package to service the user input and the submit button that gets rendered on the UI template

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired

class InputForm(FlaskForm):
    inputString = StringField('Input String', [InputRequired()])
    submit = SubmitField('Execute')
