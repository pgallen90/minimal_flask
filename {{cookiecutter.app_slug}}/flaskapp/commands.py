import os
from glob import glob
from subprocess import call

import click
from flask import current_app
from flask.cli import with_appcontext
from werkzeug.exceptions import MethodNotAllowed, NotFound

HERE = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.join(HERE, os.pardir)

@click.command()
def seed():
    from flaskapp.models.user import User

    # Setup the envronment
    from flaskapp.app import create_app
    create_app().app_context().push()
    from flaskapp.extensions import db

    # Setup a user
    new_user = User(name='Root Admin')
    new_user.email = 'patrickgallen@gmail.com'
    new_user.is_admin = True
    new_user.set_password('weakpass')
    db.session.add(new_user)
    db.session.commit()
