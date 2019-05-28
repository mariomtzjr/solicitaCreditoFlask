from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

import datetime

db = SQLAlchemy()


class Cliente(db.Model):

    __tablename__ = "Clientes"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    solicitud = db.relationship('Solicitud')
    password = db.Column(db.String(66))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, username, password, email):
        self.username = username
        self.password = self.__create_password(password)
        self.email = email

    def __create_password(self, password):
        return generate_password_hash(password)


class Solicitud(db.Model):

    __tablename__ = "Solicitudes"

    id = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.ForeignKey('cliente.id'))
    cod_cli = db.Column(db.String(10), unique=True)
    cantidad = db.Column(db.Float)
    plazo = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
