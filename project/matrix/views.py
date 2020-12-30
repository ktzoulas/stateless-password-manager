"""
    Contains the views of the 'matrix' blueprint.
"""
# pylint: disable=invalid-name
# pylint: disable=no-member

from datetime import datetime
from flask import Blueprint, abort, flash, redirect, render_template, request, url_for

from project import db
from project.matrix.forms import EditForm
from project.matrix.models import Matrix

matrix_blueprint = Blueprint('matrix', __name__, url_prefix='/matrix')


@matrix_blueprint.route('/add', methods=['GET', 'POST'])
def add():
    """Store a new matrix."""
    form = EditForm(request.form, obj=Matrix(algorithm_id=0))

    if form.validate_on_submit():
        model = Matrix(created_at=datetime.now(), modified_at=datetime.now())
        form.populate_obj(model)

        db.session.add(model)
        db.session.commit()

        flash('New matrix was created.', 'success')
        return redirect(url_for('matrix.index'))

    return render_template(
        'matrix/edit.html',
        breadcrumb=(('Home', 'main.index'), ('Matrices', 'matrix.index'), 'New Matrix'), form=form)


@matrix_blueprint.route('/delete/<int:mid>', methods=['POST'])
def delete(mid):
    """Delete matrix with the given `mid`."""
    model = Matrix.query.filter_by(id=mid).first()
    model or abort(500, "No Matrix object with '{0}' id.".format(mid))

    db.session.delete(model)
    db.session.commit()

    flash('Matrix was deleted successfully.', 'success')
    return redirect(url_for('matrix.index'))


@matrix_blueprint.route('/edit/<int:mid>', methods=['GET', 'POST'])
def edit(mid):
    """Update the fields of an existing matrix."""
    model = Matrix.query.filter_by(id=mid).first()
    model or abort(500, "No Matrix object with '{0}' id.".format(mid))

    form = EditForm(request.form, obj=model)

    if form.validate_on_submit():
        model.modified_at = datetime.now()
        form.populate_obj(model)

        db.session.commit()

        flash('Matrix was updated successfully.', 'success')
        return redirect(url_for('matrix.index'))

    return render_template(
        'matrix/edit.html',
        breadcrumb=(('Home', 'main.index'), ('Matrices', 'matrix.index'), model.name),
        form=form, id=model.id, view=False)


@matrix_blueprint.route('/')
def index():
    """List all existing matrices sorted by date of last modification in descending order."""
    return render_template('matrix/index.html', breadcrumb=(('Home', 'main.index'), 'Matrices'),
                           items=Matrix.query.order_by(Matrix.modified_at.desc()).all())


@matrix_blueprint.route('/view/<int:mid>')
def view(mid):
    """Display matrix fields."""
    model = Matrix.query.filter_by(id=mid).first()
    model or abort(500, "No Matrix object with '{0}' id.".format(mid))

    form = EditForm(obj=model)
    return render_template(
        'matrix/edit.html',
        breadcrumb=(('Home', 'main.index'), ('Matrices', 'matrix.index'), model.name),
        form=form, view=True)
