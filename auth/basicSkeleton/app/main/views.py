from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main
from .forms import NameForm
from  auth import requires_auth


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

@main.route('/secret-page')
@requires_auth
def secret_page():
    return "Secret Page"
