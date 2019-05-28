from wtforms import Form
from wtforms import StringField, IntegerField, FloatField
from wtforms.fields.html5 import EmailField


class ClienteForm(Form):
    username = StringField('username')
    email = EmailField('Correo electronico')


class SolicitudForm(Form):
    nombre = StringField('Nombre')
    cantidad = FloatField('Cantidad')
    plazo = IntegerField('Plazo')
