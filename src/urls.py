"""
urls
"""

from webapp2 import Route, SimpleRoute

ROUTES = [
    Route('/', handler='app.views.main.MainView')
]
