"""
The echo server and echo client are event-driven programs, and more generally Twisted
is an event-driven networking engine. What does that mean?
In an event-driven program, program flow is determined by external events. It is characterized 
by an event loop and the use of callbacks to trigger actions when events happen.
Contrast this structure with two other common models: single-threaded (synchronous)
and multithreaded programming.
"""
from twisted.internet import protocol, reactor
class Echo(protocol.Protocol):
    def dataReceived(self, data): #dataReceived : Called when data is received across a transport.
            print data
            self.transport.write(data)
            
class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):#method_to_buildprotocol, when connection from client made this function start
        return Echo()

reactor.listenTCP(8000, EchoFactory())
reactor.run()