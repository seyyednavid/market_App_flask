from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import  Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = "a3bda701b141e4702a2c9f8e"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)  # change string to has

from market import models
from market import routes




