"""
    Test views of the 'evaluate' blueprint.
"""
# pylint: disable=no-member

from tests import BaseTestCase


class EvaluateBlueprintTest(BaseTestCase):
    """Test functionality of the 'evaluate' blueprint"""

    def test_index_page(self):
        """test evaluating a random password"""
        form = {'password': self.fake.password()}
        response = self.client.post('/evaluate/', data=form)

        self.assertEqual(200, response.status_code)
        self.assertIn('Weak Password', str(response.data))
