from flask import Blueprint

from spaman.passwords.models import HashName

passwords_blueprint = Blueprint('passwords', __name__, url_prefix='/passwords')


@passwords_blueprint.route('/')
def index():
    models = HashName.query.all()
    return dict((model.id, model.name) for model in models)
