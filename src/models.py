from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


import sqlite3
from sqlite3 import Error
from datetime import datetime
import time

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150))
    password = db.Column(db.String(150))

