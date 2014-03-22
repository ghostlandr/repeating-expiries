"""
Workflow methods for users
"""
from google.appengine.api import users

from app.models.user import User

def get_or_create_user(name, email, user_id):
    """
    Gets the user from the datastore, or creates them if they don't exist
    """
    if not name:
        raise ValueError("name is required")
    if not email:
        raise ValueError("email is required")
    if not user_id:
        raise ValueError("user_id is required")

    import logging
    logging.info("I have these: {0} {1} {2}".format(name, email, user_id))

    key = User.build_key(user_id)

    user = key.get()
    #Useless comment
    if not user:
        kwargs = {
            'name': name,
            'email': email,
            'user_id': user_id
        }
        user = User(key=key, **kwargs)
        user.put()

    return user
