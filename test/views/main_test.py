""" Testing the views.main routes!? """
from test.fixtures.appengine import GaeTestCase

from webtest import TestApp

from main import APP

class MainViewTests(GaeTestCase):
    def setUp(self):
        super(MainViewTests, self).setUp()
        self.app = TestApp(APP)

    def tearDown(self):
        super(MainViewTests, self).tearDown()

    def test_gets_200_with_login_link(self):
        response = self.app.get('/')
        self.assertEqual(200, response.status_int)

    def test_gets_200_with_logout_link(self):
        self.testbed.setup_env(
            USER_EMAIL = "self@email.com",
            USER_ID = "123456789",
            USER_NAME = "name",
            USER_IS_ADMIN = '0',
            overwrite = True)
        response = self.app.get('/')
        self.assertEqual(200, response.status_int)
