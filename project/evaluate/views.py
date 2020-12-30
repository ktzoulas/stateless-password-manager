"""
    Contains the views of the 'evaluate' blueprint.
"""
# pylint: disable=invalid-name

from flask import Blueprint, render_template, request
from project.evaluate.forms import EvaluateForm
from project.evaluate.helpers import evaluate_pass

evaluate_blueprint = Blueprint('evaluate', __name__, url_prefix='/evaluate')


@evaluate_blueprint.route('/', methods=['GET', 'POST'])
def index():
    """ TODO: add function docstring"""
    power = None
    form = EvaluateForm(request.form)
    if form.validate_on_submit():
        if form.password.data is not None and form.password.data != '':
            power = evaluate_pass(form.password.data)

        return render_template('evaluate/index.html', form=form, power=power,
                               breadcrumb=(('Home', 'main.index'), 'Evaluate'))

    return render_template('evaluate/index.html', form=form,
                           breadcrumb=(('Home', 'main.index'), 'Evaluate'))
