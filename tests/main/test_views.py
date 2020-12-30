"""
    Test views of the 'main' blueprint.
"""
from tests import BaseTestCase


class ErrorHandlersTest(BaseTestCase):
    """Test functionality of error handlers"""

    def test_404(self):
        """test requested page not found"""
        response = self.client.get('/non_existing_page')

        self.assertEqual(200, response.status_code)
        self.assertIn('Page Not Found', str(response.data))

    def test_500(self):
        """test requested an object that does not exist in the database"""
        response = self.client.get('/matrix/edit/100')

        self.assertEqual(200, response.status_code)
        self.assertIn('Internal Server Error', str(response.data))


class MainBlueprintTest(BaseTestCase):
    """Test functionality of the 'main' blueprint."""

    def test_index_page(self):
        """test that home page is accessible"""
        response = self.client.get('/')

        self.assertEqual(200, response.status_code)
        self.assertIn('<h1>Stateless Password Manager</h1>\\n    <hr />', str(response.data))
