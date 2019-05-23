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


app = Flask(__name__)


@app.route("/")
def index():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Iniciaste Sesión"


@app.route('/login', methods=['POST'])
def admin_login():
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
    app.secret_key = os.urandom(12)
    app.run(debug=True, host="0.0.0.0", port=8000)
