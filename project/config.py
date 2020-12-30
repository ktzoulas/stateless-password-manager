"""
    Configuration parameters for the different environments (development, testing and production).
"""
# pylint: disable=too-few-public-methods

import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    """Base Configuration"""

    APP_NAME = os.getenv('APP_NAME', 'SPaMan')
    DEBUG = False
    DEBUG_TB_ENABLED = False
    LOGGING_FILE = 'spaman.log'
    LOGGING_FORMAT = '%(asctime)s %(levelname)-8s %(module)s.%(funcName)s:%(lineno)s %(message)s'
    SECRET_KEY = os.getenv('SECRET_KEY', '77c84dc23ad11ebd1e78e80acf73ce8a')
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:postgres@localhost:5432/spamandb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False


class DevelopmentConfig(BaseConfig):
    """Development Configuration"""

    DEBUG = True
    DEBUG_TB_ENABLED = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    ENV = 'development'


class TestingConfig(BaseConfig):
    """Testing Configuration"""

    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:postgres@localhost:5432/spamandb_test'
    TESTING = True


class ProductionConfig(BaseConfig):
    """Production Configuration"""

    WTF_CSRF_ENABLED = True
