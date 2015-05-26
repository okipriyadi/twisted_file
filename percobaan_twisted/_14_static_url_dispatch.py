"""
What if you'd like to serve different content at different URLs?
We can create a hierarchy of resources to serve at different URLs by registering
Resource s as children of the root resource using its putChild method. Example 4-4
demonstrates this static URL dispatch
"""

from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.static import File

root = File('/home/kyi/avionics/')
root.putChild("nyoba", File("/home/kyi/apaatuh"))
root.putChild("coba", File("/home/kyi/apaweh"))

factory = Site(root)
reactor.listenTCP(8000, factory)
reactor.run()