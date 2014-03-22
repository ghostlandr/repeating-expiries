""" Unit tests for user functions """
from test.fixtures.appengine import GaeTestCase
from google.appengine.api.users import create_logout_url, create_login_url

from app.domain.user import create_user, check_and_return_user, get_current_user, \
                             get_log_links
from app.models.user import User

class UserCreateTests(GaeTestCase):
    def setUp(self):
        super(UserCreateTests, self).setUp()
        self.name = "Testing"
        self.email = "testing@rocks.com"
        self.user_id = "123456789"

    def tearDown(self):
        super(UserCreateTests, self).tearDown()

    def test_name_required(self):
        with self.assertRaises(ValueError):
            create_user(None, None, None)

    def test_email_required(self):
        with self.assertRaises(ValueError):
            create_user(self.name, None, None)

    def test_user_id_required(self):
        with self.assertRaises(ValueError):
            create_user(self.name, self.email, None)

    def test_user_created_successfully(self):
        user = create_user(self.name, self.email, self.user_id)
        self.assertEqual(user.user_id, self.user_id)

    def test_user_getting_to_datastore_successfully(self):
        user = create_user(self.name, self.email, self.user_id)
        ndb_user = User.lookup_all_by_user_id(self.user_id)
        self.assertEqual(user.user_id, ndb_user[0].user_id)


class UserCheckAndReturnNoUsersUserTests(UserCreateTests):
    def setUp(self):
        super(UserCheckAndReturnNoUsersUserTests, self).setUp()
        self.user1 = create_user(self.name, self.email, self.user_id)

    def tearDown(self):
        super(UserCheckAndReturnNoUsersUserTests, self).tearDown()

    def test_current_user_starts_none(self):
        self.assertIsNone(get_current_user())

    def test_check_and_return_user_starts_none(self):
        user, _, _ = check_and_return_user()
        self.assertIsNone(user)

    def test_check_and_return_user_not_in_datastore(self):
        _, ndb_user, in_datastore = check_and_return_user()
        self.assertIsNone(ndb_user)
        self.assertFalse(in_datastore)


class UserCheckAndReturnWithUsersUserTests(UserCreateTests):
    def setUp(self):
        super(UserCheckAndReturnWithUsersUserTests, self).setUp()
        self.user1 = create_user(self.name, self.email, self.user_id)
        self.testbed.setup_env(
            USER_EMAIL = self.email,
            USER_ID = self.user_id,
            USER_NAME = self.name,
            USER_IS_ADMIN = '0',
            overwrite = True)

    def tearDown(self):
        super(UserCheckAndReturnWithUsersUserTests, self).tearDown()

    def test_get_current_user_returns_correct_user(self):
        self.assertEqual(get_current_user().user_id(), self.user_id)

    def test_check_and_return_user_gets_right_user(self):
        user, _, _ = check_and_return_user()
        self.assertEqual(user.user_id(), self.user_id)

    def test_check_and_return_user_gets_correct_datastore_user(self):
        _, ndb_user, in_datastore = check_and_return_user()
        self.assertIsInstance(ndb_user, list)
        self.assertEqual(ndb_user[0].user_id, self.user_id)
        self.assertTrue(in_datastore)


class LogLinksTests(UserCreateTests):
    def setUp(self):
        super(LogLinksTests, self).setUp()

    def tearDown(self):
        super(LogLinksTests, self).tearDown()

    def test_logout_link_not_none(self):
        logout_url, _ = get_log_links()
        self.assertIsNotNone(logout_url)

    def test_login_link_not_none(self):
        _, login_url = get_log_links()
        self.assertIsNotNone(login_url)
