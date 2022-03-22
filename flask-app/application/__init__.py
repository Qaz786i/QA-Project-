from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://root:{os.getenv('MYSQL_ROOT_PASSWORD')}@mysql/app-db" #'sqlite:///jobenrollment.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv ('SECRET_KEY')

db = SQLAlchemy(app)

import application.routes