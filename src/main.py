import os

import set_sys_path # Must be done first to set up path

from webapp2 import WSGIApplication
from urls import ROUTES

from app.views.filters.vurl import do_vurl

TEMPLATE_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                            'templates')

CONFIG = {
    'webapp2_extras.jinja2': {
        'filters' : {
            'vurl' : do_vurl
        },
        'template_path': TEMPLATE_DIR
    }
}


APP = WSGIApplication(ROUTES, config=CONFIG)
