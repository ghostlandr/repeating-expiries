"""
Model code
"""
from google.appengine.ext import ndb

class BaseNdbModel(ndb.Model):
    """
    Base NDB model. All models should inherit from this class, to get automatic
    created and updated fields.
    """
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)
