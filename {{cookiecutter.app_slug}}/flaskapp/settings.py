# -*- coding: utf-8 -*-
import os


class Config(object):
    """Accessible before runtime"""
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))

    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    
    APP_NAME = "{{cookiecutter.app_slug}}"

    ENVIRONMENT = os.environ.get("ENVIRONMENT")
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SERVER_NAME = os.environ.get("SERVER_NAME")

    SENDGRID_DEFAULT_FROM = os.environ.get("SENDGRID_DEFAULT_FROM")
    SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
