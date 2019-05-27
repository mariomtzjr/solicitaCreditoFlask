import os
from flask import (
    Flask,
    flash,
    redirect,
    render_template,
    request,
    session,
    abort
)

from flask_wtf import CsrfProtect
import forms
import json

from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CsrfProtect(app)


@app.route("/")
def index():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('base.html')


@app.route('/login', methods=['POST'])
def login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin@django.com':
        session['logged_in'] = True
        return index()
    else:
        flash('¡Usuario/Contraseña incorrectos!')
        return index()


@app.route("/clientes")
def listaCliente():
    return "Listado de clientes"


@app.route("/creditos")
def listaCreditos():
    return "Listado de créditos"


if __name__ == '__main__':
    # csrf.init_app(app)
    app.run(host="0.0.0.0", port=8000)
