"""
Put your Flask app code here.
"""

from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
import os

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])

# DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Handles deprecation warning
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["DATABASE_URL"]
db = SQLAlchemy(app)
migrate = Migrate(app,db)

# from models import Result
import sys
sys.path.append('src')
from html_parser import HTMLParser

@app.route('/')
def url_input():
    return render_template('url-input.html')

@app.route('/', methods=['POST'])
def url_input_post():
    url = request.form['url']
    return render_template('report.html', notices=HTMLParser(url).waqc())

if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run()
