from twisted.internet import reactor
from twisted.web.resource import Resource
from twisted.web.server import Site

class TestPage(Resource):
    isLeaf = True
    
    def render_POST(self, request):
        a = request.content.read()
        print a
        return a[::-1]

resource = TestPage()
factory = Site(resource)
reactor.listenTCP(10000, factory)
reactor.run()