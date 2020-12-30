"""
    Contains all the forms used in the blueprint.
"""
from flask_wtf import FlaskForm
from wtforms import BooleanField, IntegerField, SelectField, StringField

from project.matrix.models import Algorithm


class EditForm(FlaskForm):
    """Describe the form for adding/editing :class:`project.matrix.models.Matrix` objects."""

    name = StringField('Name')
    algorithm_id = SelectField(
        'Hash Algorithm',
        coerce=int,
        description='select the hash algorithm to be used for encoding')
    salt = StringField(
        'Salt',
        description='salts make the search space larger in the case of brute forcing')
    uppercase = BooleanField('Contains uppercase letters')
    lowercase = BooleanField('Contains lowercase letters')
    digits = BooleanField('Contains digits')
    symbols = BooleanField('Contains symbols')
    iterations = IntegerField(
        'Iterations',
        description='iterations in calculation (higher means more computation required)',
        default=1024)
    length = IntegerField('Length', default=8)

    def __init__(self, *args, **kwargs):
        super(EditForm, self).__init__(*args, **kwargs)

        # .............................specify the available options in the selection field
        self.algorithm_id.choices = [(0, '-- select a hash algorithm --')]
        self.algorithm_id.choices.extend(
            [(x.id, x.name) for x in Algorithm.query.order_by(Algorithm.name).all()])
