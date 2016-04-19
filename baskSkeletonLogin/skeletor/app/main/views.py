from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main
from .forms import NameForm, LoginForm

from flask_login import login_required, login_user

@main.route('/', methods=['GET', 'POST'])
def index():
	form = NameForm()
	if form.validate_on_submit():

		return redirect(url_for('.index'))
	else:
		pass
	return render_template('index.html',
				form=form, name=session.get('name'),
				known=session.get('known', False),
				current_time=datetime.utcnow())
@main.route("/login", methods=["GET", "POST"])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		#login and validate the user..
		user = User.query.filter_by(username=form.username.data).first()
		if user is not None:
			login_user(user, form.remember_me.data)
			return redirect(url_for('SecretPage'))
	return render_template("login.html", form=form)

@main.route('/SecretPage', methods=['GET', 'POST'])
@login_required
def SecretPage():
	
	return "Secret Page"
