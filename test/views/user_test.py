""" Testing the views.user routes!? """
from test.fixtures.appengine import GaeTestCase

from webtest import TestApp

from main import APP
from app.domain.user import create_user, check_and_return_user

class NewUserViewTests(GaeTestCase):
    def setUp(self):
        super(NewUserViewTests, self).setUp()
        self.app = TestApp(APP)
        self.email = "self@email.com"
        self.user_id = "123456789"
        self.name = "Graham Rules"
        self.testbed.setup_env(
            USER_EMAIL = self.email,
            USER_ID = self.user_id,
            USER_NAME = self.name,
            USER_IS_ADMIN = '0',
            overwrite = True)

    def tearDown(self):
        super(NewUserViewTests, self).tearDown()

    def test_new_user_gets_200(self):
        self.testbed.setup_env(
            USER_EMAIL = '',
            USER_ID = '',
            USER_IS_ADMIN = '0',
            overwrite = True)
        # Should get a 200 because they aren't redirected to home page
        response = self.app.get('/user/new')
        self.assertEqual(200, response.status_int)

    def test_returning_user_gets_redirected_to_home(self):
        create_user("name", "self@email.com", "123456789")
        response = self.app.get('/user/new')
        # If they aren't actually new, we redirect them to '/'
        self.assertEqual(302, response.status_int)

    def test_user_redirected_after_post(self):
        response = self.app.post('/user/new', {'name': self.name, 'email': self.email})
        self.assertEqual(302, response.status_int)

    def test_user_created_on_post(self):
        response = self.app.post('/user/new', {'name': self.name, 'email': self.email})
        _, ndb_user, in_datastore = check_and_return_user()
        self.assertIsNotNone(ndb_user)
        self.assertTrue(in_datastore)
