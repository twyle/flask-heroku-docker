# -*- coding: utf-8 -*-
"""This module contain the confuguration for the application."""
import os


class BaseConfig():
    """Base configuration."""

    SECRET_KEY = os.getenv('SECRET_KEY', 'secret_key')
    DEBUG = False
    TESTING = False
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    POSTGRES_HOST = os.environ['POSTGRES_HOST']
    POSTGRES_DB = os.environ['POSTGRES_DB']
    POSTGRES_PORT = os.environ['POSTGRES_PORT']
    POSTGRES_USER = os.environ['POSTGRES_USER']
    POSTGRES_PASSWORD = os.environ['POSTGRES_PASSWORD']

    db_conn_string = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    SQLALCHEMY_DATABASE_URI = db_conn_string
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(BaseConfig):
    """Configuration used during testing."""

    SECRET_KEY = os.getenv('SECRET_KEY', 'secret_key')
    DEBUG = True
    TESTING = True

    POSTGRES_HOST = os.environ['POSTGRES_HOST']
    POSTGRES_DB = f"{os.environ['POSTGRES_DB']}_test"
    POSTGRES_PORT = os.environ['POSTGRES_PORT']
    POSTGRES_USER = os.environ['POSTGRES_USER']
    POSTGRES_PASSWORD = os.environ['POSTGRES_PASSWORD']

    db_conn_string = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    SQLALCHEMY_DATABASE_URI = db_conn_string
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    """Configuration used during development."""

    SECRET_KEY = os.getenv('SECRET_KEY', 'secret_key')
    DEBUG = True
    TESTING = False

    POSTGRES_HOST = os.environ['POSTGRES_HOST']
    POSTGRES_DB = f"{os.environ['POSTGRES_DB']}_dev"
    POSTGRES_PORT = os.environ['POSTGRES_PORT']
    POSTGRES_USER = os.environ['POSTGRES_USER']
    POSTGRES_PASSWORD = os.environ['POSTGRES_PASSWORD']

    db_conn_string = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    SQLALCHEMY_DATABASE_URI = db_conn_string
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class StagingConfig(BaseConfig):
    """Configuration used during staging."""

    SECRET_KEY = os.getenv('SECRET_KEY', 'secret_key')
    DEBUG = False
    TESTING = False

    POSTGRES_HOST = os.environ['POSTGRES_HOST']
    POSTGRES_DB = f"{os.environ['POSTGRES_DB']}_stage"
    POSTGRES_PORT = os.environ['POSTGRES_PORT']
    POSTGRES_USER = os.environ['POSTGRES_USER']
    POSTGRES_PASSWORD = os.environ['POSTGRES_PASSWORD']

    db_conn_string = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    SQLALCHEMY_DATABASE_URI = db_conn_string
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(BaseConfig):
    """Configuration used during production."""

    SECRET_KEY = os.getenv('SECRET_KEY', 'secret_key')
    DEBUG = False
    TESTING = False

    POSTGRES_HOST = os.environ['POSTGRES_HOST']
    POSTGRES_DB = f"{os.environ['POSTGRES_DB']}_prod"
    POSTGRES_PORT = os.environ['POSTGRES_PORT']
    POSTGRES_USER = os.environ['POSTGRES_USER']
    POSTGRES_PASSWORD = os.environ['POSTGRES_PASSWORD']

    db_conn_string = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    SQLALCHEMY_DATABASE_URI = db_conn_string
    SQLALCHEMY_TRACK_MODIFICATIONS = False
