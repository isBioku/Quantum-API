from unittest import result
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired

class InputForm(FlaskForm):
    inputString = StringField('Input String', [InputRequired()])
    submit = SubmitField('Execute')
