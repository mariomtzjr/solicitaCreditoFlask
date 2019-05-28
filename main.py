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
from flask_sqlalchemy import SQLAlchemy

import forms

from config import DevelopmentConfig
from models import Solicitud
from models import Cliente

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CsrfProtect()

db = SQLAlchemy()


@app.route("/")
def index():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('base.html')


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        password = request.form['password']
        username = request.form['username']

        user = Cliente.query.filter_by(username=username).first()

        if user is not None and user.verify_password(password):
            success_message = "Bienvenido {}".format(username)
            flash(success_message)

            session['username'] = username
        return redirect(url_for('index'))
    else:
        flash('¡Usuario/Contraseña incorrectos!')
        return index()


@app.route("/cliente_nuevo")
def creaCliente():
    clienteForm = forms.ClienteForm(request.form)
    if request.method == 'POST' and clienteForm.validate():
        cliente = Cliente(
            username=clienteForm.username.data,
            email=clienteForm.email.data,
            password=clienteForm.password.data,
        )

    db.session.add(cliente)
    db.session.commit()

    success_message = "Usuario nuevo creado existosamente"
    flash(success_message)


@app.route("/solicitud", methods=['GET', 'POST'])
def solicitud():
    solicitudForm = forms.SolicitudForm(request.form)
    if request.method == 'POST' and solicitudForm.validate():
        user_id = session['username']
        solicitud = Solicitud(
            username=user_id,
            nombre=solicitudForm.nombre.data,
            cantidad=solicitudForm.cantidad.data
        )

    db.session.add(solicitud)
    db.session.commit()


if __name__ == '__main__':
    csrf.init_app(app)
    app.run(host="0.0.0.0", port=8000)
