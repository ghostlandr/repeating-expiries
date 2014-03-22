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
    ndb_user = None
    in_datastore = False

    if user:
        ndb_user = User.lookup_all_by_user_id(user.user_id())
        in_datastore = True if len(ndb_user) else False

    return user, ndb_user, in_datastore

def create_user(name, email, user_id, key=None):
    """
    Takes an optional key and a name, email, and user_id to create a user
    If key is not provided, one will be created from the user_id
    """
    if not name:
        raise ValueError("name is required")
    if not email:
        raise ValueError("email is required")
    if not user_id:
        raise ValueError("user_id is required")
    if not key:
        # Make our own dang key!
        key = User.build_key(user_id)

    kwargs = {
        'name': name,
        'email': email,
        'user_id': user_id
    }
    user = User(key=key, **kwargs)

    user.put()

    return user

def get_current_user():
    """ Get the current user from Google's Users API """
    return users.get_current_user()


def get_log_links():
    """ Get the log(in|out) links for a user """
    return users.create_logout_url('/'), users.create_login_url('/user/new')
