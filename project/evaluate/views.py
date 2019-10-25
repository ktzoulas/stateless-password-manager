"""
    TODO: add module docstring
"""

# pylint: disable=invalid-name

from flask import Blueprint, render_template, request
from project.evaluate.forms import EvaluateForm

evaluate_blueprint = Blueprint('evaluate', __name__, url_prefix='/evaluate')


@evaluate_blueprint.route('/', methods=['GET', 'POST'])
def index():
    """ TODO: add function docstring"""
    power = None
    form = EvaluateForm(request.form)
    if form.validate_on_submit():
        if form.password.data is not None and form.password.data != '':
            power = 'Weak Password'

        return render_template('evaluate/index.html', form=form, power=power)

    return render_template('evaluate/index.html', form=form)
