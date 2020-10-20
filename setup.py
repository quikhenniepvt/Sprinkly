# ourapp/forms.py
from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email

class SetupForm(Form):
    gpio1 = StringField('Gpio')
    desc1 = StringField('Description')
    defmin1 = StringField('Default time')
    gpio2 = StringField('Gpio')
    desc2 = StringField('Description')
    defmin2 = StringField('Default time')
    gpio3 = StringField('Gpio')
    desc3 = StringField('Description')
    defmin3 = StringField('Default time')
    gpio4 = StringField('Gpio')
    desc4 = StringField('Description')
    defmin4 = StringField('Default time')
