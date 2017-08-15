# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import (Blueprint, request, render_template, flash, url_for, send_from_directory, make_response,
                   redirect, current_app, abort)
from fuser.user_mixin import authenticate

blueprint = Blueprint('admin', __name__, url_prefix='/admin')


@blueprint.route('/')
@authenticate(mode='admin')
def home(user_obj):
    return make_response(render_template('admin_home.html', user_obj=user_obj))
