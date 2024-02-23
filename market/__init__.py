from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = "a3bda701b141e4702a2c9f8e"
db = SQLAlchemy(app)

from market import models
from market import routes




