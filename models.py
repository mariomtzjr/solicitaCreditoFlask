from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()


class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cod_cli = db.Column(db.String(10), unique=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(66))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
