from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(*args, **kwargs):
    """
        Pass the script info and return the loaded app.

    :key name: the name of the application package
    """
    app = Flask(kwargs.pop('name', __name__))
    app.config.from_object('spaman.config.Config')

    # initialize the application for the use with the database setup
    db.init_app(app)

    # import and register blueprints on the application
    from spaman.passwords.views import passwords_blueprint
    app.register_blueprint(passwords_blueprint)

    return app
