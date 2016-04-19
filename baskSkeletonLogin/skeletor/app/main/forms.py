from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import Required


class NameForm(Form):
	name = StringField('What is your name?', validators=[Required()])
	submit = SubmitField('Submit')

class LoginForm(Form):
	username = StringField('Your Username:', validators=[Required()])
	password = PasswordField('Password', validators=[Required()])
	remember_me = BooleanField('Keep me logged in')
	submit = SubmitField('Log In')

