""" workflow.user unit tests """
from test.fixtures.appengine import GaeTestCase

from app.domain.user import create_user
from app.models.user import User
from app.workflow.user import get_or_create_user

class UserGetOrCreateTests(GaeTestCase):
    def setUp(self):
        super(UserGetOrCreateTests, self).setUp()
        self.name = "Testing"
        self.email = "testing@rocks.com"
        self.user_id = "123456789"
        self.name2 = "Testing2"
        self.email2 = "testing@muchrocks.com"
        self.user_id2 = "987654321"
        self.user2 = create_user(self.name2, self.email2, self.user_id2)

    def tearDown(self):
        super(UserGetOrCreateTests, self).setUp()

    def test_name_is_required(self):
        with self.assertRaises(ValueError):
            get_or_create_user(None, None, None)

    def test_email_is_required(self):
        with self.assertRaises(ValueError):
            get_or_create_user(self.name, None, None)

    def test_user_id_is_required(self):
        with self.assertRaises(ValueError):
            get_or_create_user(self.name, self.email, None)

    def test_user_is_returned_if_exists(self):
        user = get_or_create_user(self.name2, self.email2, self.user_id2)
        # User should already be created in setUp
        self.assertEqual(user.name, self.name2)
        self.assertEqual(user.email, self.email2)
        self.assertEqual(user.user_id, self.user_id2)

    def test_new_user_created_if_does_not_exist(self):
        user = get_or_create_user(self.name, self.email, self.user_id)
        self.assertEqual(user.name, self.name)
        self.assertEqual(user.email, self.email)
        self.assertEqual(user.user_id, self.user_id)

    
