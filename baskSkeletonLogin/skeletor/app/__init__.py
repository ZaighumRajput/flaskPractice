# This is where teh application factory function lives
# Import all the necessary Flask extenstions here

from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask_login import LoginManager

import pdb
from config import config

login_manager = LoginManager()
#login_manager._session_protection = "strong"
bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	pdb.set_trace()

	bootstrap.init_app(app)
	login_manager.init_app(app)
        db.init_app(app)
	from main import main as main_blueprint
	app.register_blueprint(main_blueprint)

	return app
