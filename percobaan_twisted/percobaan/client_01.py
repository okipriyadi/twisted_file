from twisted.internet import reactor, protocol

class EchoClient(protocol.Protocol):
    def __init__(self, puisi):
        self.puisi = puisi
    def connectionMade(self): #ConnectionMade : Called when a connection to another endpoint is made.
        self.transport.write("Hello, world!")
    def dataReceived(self, data):
        print "Server said:", data
        self.puisi = self.puisi + data
        self.transport.loseConnection()
        
class EchoFactory(protocol.ClientFactory):
    
    def __init__(self,puisi):
        self.puisi = puisi    
    def buildProtocol(self, addr):
        print "addr =", addr  
        return EchoClient(self.puisi)
    def clientConnectionFailed(self, connector, reason):
        print "Connection failed."
        reactor.stop()
    def clientConnectionLost(self, connector, reason):
        print "Connection lost."
        reactor.stop()

puisi = ""
reactor.connectTCP("localhost", 8000, EchoFactory(puisi))
reactor.run()


