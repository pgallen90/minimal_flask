# -*- coding: utf-8 -*-
import os


class RootConfig(object):
    """Accessible before runtime"""
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))

    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    

class ProdConfig(RootConfig):
    """Production configuration."""
    ENVIRONMENT = 'prod'
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SERVER_NAME = os.environ.get("SERVER_NAME")


class DevConfig(RootConfig):
    """Production configuration."""
    ENVIRONMENT = 'dev'
    SECRET_KEY = 'A SECRET'
    SERVER_NAME = 'streak.local:5000'