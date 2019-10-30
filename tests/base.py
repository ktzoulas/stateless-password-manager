"""
    Contains common classes used in various test scenarios.
"""
# pylint: disable=no-member

import os
import warnings

from datetime import datetime
from faker import Faker
from flask_testing import TestCase

from project import create_app, db
from project.matrix.models import Algorithm, Matrix


def commit():
    """Commit record changes - rollback in case of error."""
    try:
        db.session.commit()

    except Exception as err:
        print('Failed to commit record changes - {} [{}]'.format(err, err.__class__.__name__))

        db.session.rollback()
        return False
    return True


class BaseTestCase(TestCase):
    """
        This class contains the basic `setUp` and `tearDown` actions that must be performed before
    and after each test scenario is executed.
    """

    def create_app(self):
        warnings.filterwarnings('ignore', category=DeprecationWarning)
        return create_app(settings='project.config.TestingConfig')

    def setUp(self):
        db.create_all()

        init_schemas = InitSchemas()
        init_schemas.initialize_algorithm()
        init_schemas.generate_fake_matrices()
        self.fake = Faker()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

        if os.path.isfile(self.app.config.get('LOGGING_FILE')):
            os.remove(self.app.config.get('LOGGING_FILE'))


class InitSchemas:
    """Initialize table schemas in current database."""

    ALGORITHMS = ('md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512')

    def generate_fake_matrices(self):
        """Generate fake data for 'matrix' table."""
        matrices = (
            ('Gmail', 4, 'fd70e5b3b577a1572436847b8e65875e', None, None),
            ('Facebook', 6, '60a8ec4be6ab4b909ea811a18156781c', 2048, None),
            ('Instagram', 1, 'a1791e97739c206a7bb09ddff3ecb51d', 512, 8),
            ('LinkedIn', 2, '0e9c6984dfc3ad02827f0c67288b0bc5', 4096, 32),
            ('Codecademy', 5, 'a7c331d5c1a75b0894871da345ac05db', 4096, 12),
            ('Slack', 3, '5d7549459403b55798c3e713facfeea4', 128, None)
        )

        for name, algorithm_id, salt, iterations, length in matrices:
            db.session.add(
                Matrix(name=name, algorithm_id=algorithm_id, salt=salt, created_at=datetime.now(),
                       modified_at=datetime.now()))

        print(self.generate_fake_matrices.__doc__)
        return commit()

    def initialize_algorithm(self):
        """Initialize 'algorithm' table."""
        _ = [db.session.add(Algorithm(name=x)) for x in self.ALGORITHMS]

        print(self.initialize_algorithm.__doc__)
        return commit()
