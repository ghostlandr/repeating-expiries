""" Unit tests for models.user """
from test.fixtures.appengine import GaeTestCase

from app.domain.user import create_user
from app.models.user import User

class UserLookupTests(GaeTestCase):
    def setUp(self):
        super(UserLookupTests, self).setUp()
        self.name = "Testing"
        self.email = "testing@rocks.com"
        self.user_id = "123456789"
        self.user1 = create_user(self.name, self.email, self.user_id)
        self.name2 = "Testing2"
        self.email2 = "testing@muchrocks.com"
        self.user_id2 = "987654321"
        self.user2 = create_user(self.name2, self.email2, self.user_id2)

    def tearDown(self):
        super(UserLookupTests, self).tearDown()

    def test_lookup_all_limit_must_be_int(self):
        with self.assertRaises(ValueError):
            User.lookup_all(limit="50")
            User.lookup_all(limit=50.0)

    def test_lookup_by_user_id_requires_user_id(self):
        with self.assertRaises(ValueError):
            User.lookup_all_by_user_id(None)

    def test_lookup_user_by_user_id(self):
        user = User.lookup_all_by_user_id(self.user_id)
        self.assertEqual(user[0].user_id, self.user_id)
        user2 = User.lookup_all_by_user_id(self.user_id2)
        self.assertEqual(user2[0].user_id, self.user_id2)

    def test_looking_up_correct_user_by_id(self):
        user = User.lookup_all_by_user_id(self.user_id)
        self.assertNotEqual(user[0].user_id, self.user_id2)

    def test_looking_up_correct_number_of_users(self):
        users = User.lookup_all()
        # Equal to two because two are created in setUp
        self.assertEqual(2, len(users))
