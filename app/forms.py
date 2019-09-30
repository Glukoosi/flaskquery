from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, RadioField, SelectField
from wtforms.validators import DataRequired, InputRequired
from markupsafe import Markup

class Form(FlaskForm):
    name = StringField('Nimi', validators=[DataRequired()])
    mail = StringField('Sähköpostiosoite', validators=[DataRequired()])
    phone = StringField('Puhelinnumero', validators=[DataRequired()])
    start = RadioField('Bussiin nousu paikka', choices=(['yliopisto', 'Yliopisto'],['tuira', 'Tuira'],['linja-autoasema','Linja-autoasema']), validators=[InputRequired()])
    status = RadioField('Olen', choices=(['fuksi', 'Fuksi'],['pro', 'RRO'],['hallituslainen','Hallituslainen'],['koops','koops'],['teekkari','Teekkari']), validators=[InputRequired()])
    public = BooleanField('Nimeni saa julkaista')
    consent = BooleanField(
        'Hyväksyn henkilötietojeni käsittelyn tietosuojaselosteen mukaisesti.',
        validators=[InputRequired()])
    submit = SubmitField("Lähetä")
