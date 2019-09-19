from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, RadioField, SelectField
from wtforms.validators import DataRequired, InputRequired
from markupsafe import Markup

class Form(FlaskForm):
    name = StringField('Nimi', validators=[DataRequired()])
    year = StringField('Opintojen aloitusvuosi')
    mail = StringField('Sähköpostiosoite', validators=[DataRequired()])
    nonalcoholic = BooleanField('Alkoholiton')
    food = StringField('Erityisruokavalio')
    speechbox = BooleanField('Haluan pitää puheenvuoron')
    speech = StringField('Edustamani taho tai puheenvuoron aihe')
    other = StringField('Vapaa sana')
    public = BooleanField('Nimeni saa julkaista')
    consent = BooleanField(
        'Hyväksyn henkilötietojeni käsittelyn tietosuojaselosteen mukaisesti.',
        validators=[InputRequired()])
    submit = SubmitField("Lähetä")
