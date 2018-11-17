from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, RadioField, TextAreaField
from wtforms.validators import DataRequired

class Form(FlaskForm):
    string = StringField('StringField (data required)', validators=[DataRequired()])
    boolean = BooleanField('BooleanField')
    radio = RadioField('RadioField', choices=(['Choice1', 'Choice1'],['Choice2', 'Choice2']))
    text = TextAreaField('TextArea')
    submit = SubmitField('Submit')
