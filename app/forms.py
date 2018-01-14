from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, RadioField, TextAreaField
from wtforms.validators import DataRequired, Email, Required

class RegForm(FlaskForm):
    name = StringField('Nimi', validators=[DataRequired()])
    email = StringField('Sähköposti', validators=[Email()])
    representative = StringField('Edustava taho/joukkue', validators=[DataRequired()])
    greeting = BooleanField('Haluatko tuoda tervehdyksen?')
    food = StringField('Erityisruokavalio')
    alcohol = RadioField('Holiton / Holillinen', choices=(['Holillinen', 'Holillinen (20e)'],['Holiton', 'Holiton (20e)']), validators=[Required()])
    gambina = BooleanField('Iso G (+9,83 € hintaan)')
    avec = StringField('Avec / Pöytätoive (avec ilmoittautuu erikseen)')
    free = TextAreaField('Vapaa sana')
    submit = SubmitField('Ilmoittaudu')

class RegSwagForm(FlaskForm):
    name = StringField('Nimi', validators=[DataRequired()])
    email = StringField('Sähköposti', validators=[Email()])
    greeting = BooleanField('Haluatko tuoda tervehdyksen?')
    food = StringField('Erityisruokavalio')
    alcohol = RadioField('Holiton / Holillinen', choices=(['Holillinen', 'Holillinen (20e)'],['Holiton', 'Holiton (20e)']), validators=[Required()])
    gambina = BooleanField('Iso G (+9,83 € hintaan)')
    avec = StringField('Avec / Pöytätoive (avec ilmoittautuu erikseen)')
    free = TextAreaField('Vapaa sana')
    submit = SubmitField('Ilmoittaudu')
