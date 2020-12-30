"""
    Contains the blueprint's form
"""
from flask_wtf import FlaskForm
from wtforms import PasswordField


class EvaluateForm(FlaskForm):
    """The evaluation form with only 1 input"""

    password = PasswordField(
        'Password',
        description='enter a password for evaluation')
