"""Create an application instance."""
from flask.helpers import get_debug_flag

from flaskapp.app import create_app
from flaskapp.settings import Config

app = create_app(Config)