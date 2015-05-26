"""
CalendarHome.getChild describes how to traverse a URL from left to right until we get
a renderable resource. If there is no additional component to the requested URL (i.e.,
the request was for / ), CalendarHome returns itself to be rendered by invoking its
render_GET method. If the URL has an additional component to its path that is an
integer, an instance of YearPage is rendered. If that path component couldn't be converted 
to a number, an instance of twisted.web.error.NoResource is returned instead,
which will render a generic 404 page.
"""
from twisted.internet import reactor
from twisted.web.resource import Resource, NoResource
from twisted.web.server import Site
from calendar import calendar

class YearPage(Resource):
    def __init__(self, year):
        Resource.__init__(self)
        self.year = year

    def render_GET(self, request):
        return "<html><body><pre>%s</pre></body></html>" % (calendar(self.year),)

class CalendarHome(Resource):
    def getChild(self, name, request):
        if name == '':
            return self
        if name.isdigit():
            return YearPage(int(name))
        else:
            return NoResource()
     
    def render_GET(self, request):
        return "<html><body>Welcome to the calendar server!</body></html>"

root = CalendarHome()
factory = Site(root)
reactor.listenTCP(10001, factory)
reactor.run()