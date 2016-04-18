# This is where teh application factory function lives
# Import all the necessary Flask extenstions here

from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.mail import Mail
from config import config

import pdb

bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()

def create_app(config_name):
	pdb.set_trace()
	app = Flask(__name__)
	app.config.from_object(config[config_name])

	bootstrap.init_app(app)
	mail.init_app(app)
        db.init_app(app)
	from main import main as main_blueprint
	app.register_blueprint(main_blueprint)

	return app
