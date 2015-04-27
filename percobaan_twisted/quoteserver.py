from twisted.internet.protocol import Factory
from twisted.internet import reactor, protocol
class QuoteProtocol(protocol.Protocol):
    def __init__(self, factory):
        self.factory = factory
    
    def connectionMade(self): #Called when a connection to another endpoint is made.
        self.factory.numConnections += 1
        print "MADE self.factory.numConnections", self.factory.numConnections

    def dataReceived(self, data): #Called when data is received across a transport.
        print "Number of active connections: %d" % (self.factory.numConnections,)
        print "> Received: ``%s''\n> Sending: ``%s''" % (data, self.getQuote())
        self.transport.write(self.getQuote())
        self.updateQuote(data)

    def connectionLost(self, reason):#Called when the connection is shut down.
        self.factory.numConnections -= 1
        print "LOST self.factory.numConnections", self.factory.numConnections
    
    def getQuote(self):
        return self.factory.quote

    def updateQuote(self, quote):
        self.factory.quote = quote

class QuoteFactory(Factory):
    numConnections = 0
    def __init__(self, quote=None):
        self.quote = quote or "An apple a day keeps the doctor away"

    def buildProtocol(self, addr):
        return QuoteProtocol(self)

reactor.listenTCP(8000, QuoteFactory())
reactor.run()