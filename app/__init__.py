from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask import Flask, request, render_template

app = Flask(__name__)
CORS(app)

# Configurations
app.config.from_object('config')

# Define the database object
db = SQLAlchemy(app)

from app import views
from app import models
from app import controllers
