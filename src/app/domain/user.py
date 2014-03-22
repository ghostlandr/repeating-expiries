"""
Domain functions for users
"""
from google.appengine.api import users

from app.models.user import User

def check_and_return_user():
    """
    Returns a Users.user object, an ndb_user, and whether or not they exist in datastore
    """
    user = users.get_current_user()

    if user:
        ndb_user = User.lookup_all_by_user_id(user.user_id())
        in_datastore = True if len(ndb_user) else False

    return user, ndb_user, in_datastore

def get_current_user():
    """ Get the current user from Google's Users API """
    return users.get_current_user()


def get_log_links():
    """ Get the log(in|out) links for a user """
    return users.create_logout_url('/'), users.create_login_url('/user/new')
