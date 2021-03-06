# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import (Blueprint, request, render_template, flash, url_for, send_from_directory, make_response,
                   redirect, current_app, abort)
from fuser.user_mixin import authenticate


blueprint = Blueprint('public', __name__)


@blueprint.route('/')
@authenticate(mode='public')
def home():
	return make_response(render_template('home.html'))


