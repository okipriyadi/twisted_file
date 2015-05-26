"""
The FormPage Resource in handle_post.py implements both render_GET and
render_POST methods.
render_GET returns the HTML for a blank page with a text box called "form-field" .
When a visitor visits http://localhost:8000, she will see this form.
render_POST extracts the text inputted by the user from request.args , sanitizes it with
cgi.escape , and returns HTML displaying what the user submitted.
"""

from twisted.internet import reactor
from twisted.web.resource import Resource
from twisted.web.server import Site
import cgi

class FormPage(Resource):
    isLeaf = True
    def render_GET(self, request):
        return """
                <html>
                <body>
                <form method="POST">
                <input name="form-field" type="text" />
                <input type="submit" />
                </form>
                </body>
                </html>
                """
    def render_POST(self, request):
        return """
                <html>
                <body>You submitted: %s</body>
                </html>
                """ % (cgi.escape(request.args["form-field"][0]),)
factory = Site(FormPage())
reactor.listenTCP(8000, factory)
reactor.run()               
    