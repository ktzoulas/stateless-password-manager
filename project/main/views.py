"""
    Contains the views of the 'main' blueprint.
"""
# pylint: disable=invalid-name

from flask import Blueprint, render_template

main_blueprint = Blueprint('main', __name__)


@main_blueprint.route('/')
def index():
    """TODO: add function docstring"""
    return render_template('main/index.html', breadcrumb=('Home',))
