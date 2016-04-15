# This is where the application starts
import os

#from app.models import User, Role
from flask.ext.script import Manager, Shell
from app import create_app



app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)


if __name__ == '__main__':
    manager.run()
