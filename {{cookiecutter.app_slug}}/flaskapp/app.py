from flask import Flask, render_template
import os

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flaskapp.extensions import db

from importlib import import_module

from flask.blueprints import Blueprint

from flaskapp import commands
from flaskapp.settings import Config

# UNTESTED: From https://www.youtube.com/watch?v=1ByQhAM5c1I
from werkzeug.utils import find_modules, import_string
from fuser import Fuser

def register_blueprints(app):
    for name in find_modules('flaskapp.blueprints'):
        mod = import_string(name)
        if hasattr(mod, 'blueprint'):
            app.register_blueprint(mod.blueprint)
    
# Replace this
def load_blueprints_from_path(app, packages_path='./flaskapp/blueprints'):
    blueprints = []
    for name in os.listdir(packages_path):
        if name != '__init__.py':

            path, base_name = os.path.split(packages_path)
            package_name = name[:-3]

            try:
                package = import_module('flaskapp.{}.{}'.format(base_name, package_name))
                module = getattr(package, 'blueprint')
                if isinstance(module, Blueprint):
                    blueprints.append(module)
                    app.register_blueprint(module)
                    print("Blueprint Installed: {}".format(package_name))
            except (ImportError, AttributeError) as e:
                pass

    return blueprints


def register_commands(app):
    """Register Click commands."""
    app.cli.add_command(commands.seed)


def create_app(config_object=Config):
    app = Flask(__name__)
    app.config.from_object(config_object)

    db.init_app(app)
    migrate = Migrate(app, db)

    from flaskapp.models.user import User
    fuser = Fuser(app)

    register_blueprints(app)
    register_commands(app)

    from bootstrap_macros import BootstrapMacros
    BootstrapMacros(app)

    return app
