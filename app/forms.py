from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, RadioField, SelectField
from wtforms.validators import DataRequired, InputRequired

class Form(FlaskForm):
    name = StringField('Nimi*', validators=[DataRequired()])
    guild = RadioField('Kilta*', choices=(['otit', 'OTiT'],['sik', 'SIK']))
    mail = StringField('Sähköpostiosoite*', validators=[DataRequired()])
    phone = StringField('Puhelinnumero*', validators=[DataRequired()])
    place = SelectField('Lähtöpaikka*', choices=(['yliopisto', 'Yliopisto'], ['tuira', 'Tuira'], ['linja-autoasema', 'Linja-autoasema']), validators=[DataRequired()])
    consent = BooleanField(
        'Hyväksyn henkilötietojeni käsittelyn tietosuojaselosteen mukaisesti, sekä ymmärrän ilmoittatumisen olevan sitova.',
        validators=[InputRequired()])
    submit = SubmitField('Lähetä')
