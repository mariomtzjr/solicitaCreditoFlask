from wtforms import Form
from wtforms import StringField
from wtforms.fields.html5 import EmailField


class ClienteForm(Form):
    cod_cli = StringField('cod_cli')
    username = StringField('username')
    email = EmailField('Correo electronico')
