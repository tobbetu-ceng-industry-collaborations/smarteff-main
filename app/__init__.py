from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define the database object
db = SQLAlchemy(app)

from app import views
from app import models
from app import controllers
