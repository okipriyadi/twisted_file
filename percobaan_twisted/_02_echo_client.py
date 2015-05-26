"""
The clients job is to connect to the server, send it a message, receive a response, 
and terminate the connection.
"""
from twisted.internet import reactor, protocol
class EchoClient(protocol.Protocol):
    def connectionMade(self): #ConnectionMade : Called when a connection to another endpoint is made.
        self.transport.write("Hello, world!")
    def dataReceived(self, data):
        print "Server said:", data
        self.transport.loseConnection()
        
class EchoFactory(protocol.ClientFactory):
    def buildProtocol(self, addr):
        print "addr =", addr  
        return EchoClient()
    def clientConnectionFailed(self, connector, reason):
        print "Connection failed."
        reactor.stop()
    def clientConnectionLost(self, connector, reason):
        print "Connection lost."
        reactor.stop()

print "reactor start"        
reactor.connectTCP("localhost", 8000, EchoFactory())
reactor.run()