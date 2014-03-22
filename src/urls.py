"""
urls
"""

from webapp2 import Route, SimpleRoute

ROUTES = [
    Route('/', handler='app.views.main.MainView'),
    Route('/user/new', handler='app.views.user.NewUserView')
]
