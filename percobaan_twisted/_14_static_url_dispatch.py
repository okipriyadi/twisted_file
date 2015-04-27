from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.static import File

root = File('/home/avionics/testweb')
root.putChild("doc", File("/home/avionics/testweb2"))
root.putChild("logs", File("/home/avionics/testweb3"))

factory = Site(root)
reactor.listenTCP(8000, factory)
reactor.run()