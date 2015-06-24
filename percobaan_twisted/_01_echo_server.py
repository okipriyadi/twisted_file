"""
The echo server and echo client are event-driven programs, and more generally Twisted
is an event-driven networking engine. What does that mean?
In an event-driven program, program flow is determined by external events. It is characterized 
by an event loop and the use of callbacks to trigger actions when events happen.
Contrast this structure with two other common models: single-threaded (synchronous)
and multithreaded programming.

TCP echo servers job is to listen for TCP connections on a particular port and echo back anything
it receives 
"""
from twisted.internet import protocol, reactor
from twisted.protocols.basic import LineOnlyReceiver
#class Echo(protocol.Protocol):#our own Echo protocol by subclassing protocol.Protocol
class Echo(LineOnlyReceiver):#our own Echo protocol by subclassing protocol.Protocol
    #def dataReceived(self, data): #dataReceived : Called when data is received across a transport.
    #        print "data =", repr(data), "finished"
    #        self.transport.write(data)
    def lineReceived(self, line):
            print "data =", repr(line), "finished"
            self.transport.write(line)
class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):#method_to_buildprotocol, when connection from client made this function start
        print "addr =", addr
        return Echo()
    # karna build protocol hanya me-return protocol maka cara shortcut selain memakai buildProtolo yaitu
    # dalam contoh kasus diatas method buildProtocol bisa dihilangkan dan diganti dengan protocol = Echo() 
print "reactor start"
reactor.listenTCP(8000, EchoFactory())
reactor.run()