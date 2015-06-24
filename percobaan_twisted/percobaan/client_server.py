from twisted.internet import reactor, protocol

class Echo(protocol.Protocol):#our own Echo protocol by subclassing protocol.Protocol
    def __init__(self, puisi):
        self.puisi = puisi
    def dataReceived(self, data): #dataReceived : Called when data is received across a transport.
            print "data =", data
            print "self.puisi =",self.puisi 
            self.transport.write("self.puisi = %s" % self.puisi)
            
class EchoFactory(protocol.Factory):
    def __init__(self, puisi):
        self.puisi = puisi
        
    def buildProtocol(self, addr):#method_to_buildprotocol, when connection from client made this function start
        print "addr =", addr
        return Echo(self.puisi)

class EchoClient(protocol.Protocol):
    def __init__(self, puisi):
        self.puisi = puisi
    def connectionMade(self): #ConnectionMade : Called when a connection to another endpoint is made.
        self.transport.write("Hello, world! =%s" %self.puisi)
        
    def dataReceived(self, data):
        self.puisi.append(data)
        print "Server said:", self.puisi
        print "================="
        self.transport.loseConnection()
        
class EchoClientFactory(protocol.ClientFactory):
    
    def __init__(self, puisi):
        self.puisi = puisi    
    def buildProtocol(self, addr):
        print "addr =", addr  
        return EchoClient(self.puisi)
    def clientConnectionFailed(self, connector, reason):
        print "Connection failed."
        reactor.stop()
    def clientConnectionLost(self, connector, reason):
        print "Connection lost."
        #reactor.stop()

puisi = []
reactor.connectTCP("localhost", 46740, EchoClientFactory( puisi ))
reactor.listenTCP(8000, EchoFactory(puisi))
reactor.run()