from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from markupsafe import Markup

class Form(FlaskForm):
    url = StringField('Alkuperäinen URL', validators=[DataRequired()])
    short = StringField('Lyhenne', validators=[DataRequired()])
    public = BooleanField('Listaa osoite tälle sivustolle.', default=True)
    premium = BooleanField('Virallinen osoite')
    premiumpass = PasswordField('Salasana')

    submit = SubmitField('Lyhennä')