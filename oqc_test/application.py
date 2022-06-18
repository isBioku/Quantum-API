from flask import Flask
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)
application.config['SECRET_KEY'] = '8b2f8ef902ca5d19d792102e995ea29e'
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///model.db'
db = SQLAlchemy(application)
db.create_all()
from oqc_test import routes