import unittest
from . import TestBase


class AppTest(TestBase):

    def test_app_configuration(self):
        self.assertTrue(self.app.config['TESTING'])

class UserResourceTest(TestBase):

    def test_user_get_empty_db(self):
        rv = self.client.get('/users')
        self.assertTrue('[]', rv.data)
