"""
View code
"""

from webapp2 import RequestHandler, cached_property
from webapp2_extras import jinja2


class TemplatedView(RequestHandler):
    """
    Base view for all other views to extend
    """

    @cached_property
    def jinja2(self):
        """
        Get that jinja fired up
        """
        return jinja2.get_jinja2(app=self.app)

    def render_response(self, template, **context):
        """ Pass a template (html) and a dictionary """
        content = self.jinja2.render_template(template, **context)
        self.response.write(content)
