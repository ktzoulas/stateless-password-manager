"""
    Implements a WSGI application that acts as the central object.
"""
# pylint: disable=invalid-name

import logging
import os

from logging.handlers import RotatingFileHandler

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
db = SQLAlchemy()
toolbar = DebugToolbarExtension()


def create_app(**kwargs):
    """
        Create a new WSGI application, register blueprints and initialize extensions.

    :key name    : The name of the Flask application.
    :key settings: The object with that name will be imported to set environment variables.
    """
    app = Flask(kwargs.pop('name', os.getenv('APP_NAME', __name__)))

    # .................................set configuration
    app.config.from_object(kwargs.pop(
        'settings', os.getenv('APP_SETTINGS', 'project.config.DevelopmentConfig')))

    # .................................set up extensions
    bootstrap.init_app(app)
    db.init_app(app)
    toolbar.init_app(app)

    # .................................configure logging
    app = create_handler(app, maxBytes=10 * 1024 * 1024, backupCount=10)

    # .................................register blueprints
    from project.main.views import main_blueprint
    from project.matrix.views import matrix_blueprint
    from project.evaluate.views import evaluate_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(matrix_blueprint)
    app.register_blueprint(evaluate_blueprint)

    @app.errorhandler(404)
    def page_not_found(error):
        """Redirect to a custom page when the return status code is 404."""
        app.logger.error('No "{0.path}" page found - {1}'.format(request, error))
        return render_template('errors/404.html')

    @app.errorhandler(500)
    def internal_server_error(error):
        """Redirect to a custom page when the return status code is 500."""
        app.logger.error(error)
        return render_template('errors/500.html')

    return app


def create_handler(app, **kwargs):
    """
        Create a handler for logging to a set of files, which switches from one file to the next
    when the current file reaches a certain size.
    """
    handler = RotatingFileHandler(app.config['LOGGING_FILE'], **kwargs)
    handler.setLevel(
        logging.DEBUG if (app.config['DEBUG'] or app.config['TESTING']) else logging.INFO)
    handler.setFormatter(logging.Formatter(app.config['LOGGING_FORMAT']))

    app.logger.addHandler(handler)
    return app
