#!/usr/bin/env python
"""
    TODO: add module docstring
"""
# pylint: disable=invalid-name

import sys
import time
import unittest

from coverage import coverage
from flask.cli import FlaskGroup

from project import create_app, db
from tests.base import InitSchemas

# app = create_app()
cli = FlaskGroup(create_app=create_app)
cov = coverage(branch=True, include='project/*', omit=[
    'project/config.py',
    'project/__init__.py',
    'project/*/__init__.py'
])
cov.start()


def _execute_unittests():
    """Run the unittests."""
    try:
        tests = unittest.TestLoader().discover('tests')
        result = unittest.TextTestRunner(verbosity=2).run(tests)

        assert result.wasSuccessful()

    except AssertionError:
        sys.exit(1)

    finally:
        cov.stop()
        cov.save()


@cli.command()
def generate_sample_data():
    """Feed the database with sample data."""
    init_schemas = InitSchemas()
    init_schemas.initialize_algorithm()
    init_schemas.generate_fake_matrices()


@cli.command()
def init_db():
    """Clear the database and create a new schema."""
    print('[*] Drops all tables...')
    db.drop_all()

    print('[*] Creates all tables, again...')
    db.create_all()

    print('DONE')


@cli.command()
def test():
    """Run the unittests without coverage."""
    _execute_unittests()


@cli.command()
def test_with_coverage():
    """Run the unittests with coverage."""
    _execute_unittests()
    time.sleep(1)  # ..................avoid collapse

    print('Coverage Summary:')
    cov.report()
    cov.html_report()
    cov.erase()


if __name__ == '__main__':
    cli()
