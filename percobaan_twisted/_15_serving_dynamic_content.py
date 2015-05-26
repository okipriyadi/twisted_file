"""
Serving dynamic content looks very similar to serving static content, the big difference
is that instead of using an existing Resource , like File , you'll subclass Resource to define
the new dynamic resource you want a Site to serve.

ClockPage is a subclass of Resource . We implement a render_ [method] for every HTTP
method we want to support; in this case we only care about supporting GET requests,so render_GET is all we implement
If we were to POST to this web server, we'd get a
405 Method Not Allowed unless we also implemented render_POST .

The rendering method is passed the request made by the client. This is not an instance
of twisted.web.http.Request , as in Example 4-2; it is instead an instance of
twisted.web.server.Request , which subclasses http.Request and understands
application-layer ideas like session management and rendering.
"""

from twisted.internet import reactor
from twisted.web.resource import Resource
from twisted.web.server import Site

import time
class ClockPage(Resource):
    isLeaf = False
    def render_GET(self, request):
        return "The local time is %s" % (time.ctime(),)

resource = ClockPage()
factory = Site(resource)
reactor.listenTCP(8000, factory)
reactor.run()