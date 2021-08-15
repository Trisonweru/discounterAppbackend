from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app=Flask(__name__)

app.config['SECRET_KEY']="this is some super secret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///discounts.db' 

db = SQLAlchemy(app)
CORS(app)

from Application import routes