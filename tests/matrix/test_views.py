"""
    Test views of the 'matrix' blueprint.
"""
# pylint: disable=no-member
from tests import BaseTestCase
from project.matrix.models import Matrix


class MatrixBlueprintTest(BaseTestCase):
    """Test functionality of the 'matrix' blueprint"""

    def test_add_page(self):
        """test create a new matrix"""
        form = {'name': self.fake.company(), 'algorithm_id': 4, 'salt': self.fake.md5()}
        response = self.client.post('/matrix/add', data=form, follow_redirects=True)

        self.assertEqual(200, response.status_code)
        self.assertIn('New matrix was created.', str(response.data))

        # .............................test database entry exists
        self.assertIsInstance(Matrix.query.filter_by(name=form['name']).first(), Matrix)

    def test_delete_page(self):
        """test delete a matrix giving its `id`"""
        model = Matrix.query.first()
        response = self.client.post('/matrix/delete/{0.id}'.format(model), follow_redirects=True)

        self.assertEqual(200, response.status_code)
        self.assertIn('Matrix was deleted successfully.', str(response.data))

        # .............................test database entry does not exist
        self.assertIsNone(Matrix.query.filter_by(id=model.id).first())

    def test_edit_page(self):
        """test update the values of an existing matrix"""
        model = Matrix.query.first()
        form = {
            'name': '{0.name}_edited'.format(model),
            'algorithm_id': model.algorithm_id,
            'salt': model.salt,
            'length': model.length + 8
        }

        response = self.client.post('/matrix/edit/{0.id}'.format(model), data=form,
                                    follow_redirects=True)

        self.assertEqual(200, response.status_code)
        self.assertIn('Matrix was updated successfully.', str(response.data))

        # .............................test database entry is updated
        self.assertEqual(model.name, Matrix.query.filter_by(id=model.id).first().name)
        self.assertEqual(model.length, Matrix.query.filter_by(id=model.id).first().length)

    def test_index_page(self):
        """test all existing matrices are listed in descending order"""
        models = Matrix.query.order_by(Matrix.modified_at.desc()).all()
        ordered_names = '.*'.join([r'{0.name}\\n\s+</a>'.format(x) for x in models])
        response = self.client.get('/matrix/')

        self.assertEqual(200, response.status_code)
        self.assertRegex(str(response.data), ordered_names)

    def test_view_page(self):
        """test display fields of matrix"""
        model = Matrix.query.first()
        response = self.client.get('/matrix/view/{0.id}'.format(model))

        self.assertEqual(200, response.status_code)
        self.assertRegex(str(response.data), 'disabled id="name".*value="{0.name}"'.format(model))
