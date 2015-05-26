"""
Often, the connection of a client will be lost unintentionally due to network problems. One way to reconnect after a
disconnection would be to call connector.connect() when the connection is lost:
from twisted.internet.protocol import ClientFactory
class EchoClientFactory(ClientFactory):
def clientConnectionLost(self, connector, reason):
connector.connect()

However, most programs that want this functionality should implement ReconnectingClientFactory instead, which
tries to reconnect if a connection is lost or fails and which exponentially delays repeated reconnect attempts.
"""
from twisted.internet.protocol import Protocol, ReconnectingClientFactory
from sys import stdout
class Echo(Protocol):
    def dataReceived(self, data):
        stdout.write(data)

class EchoClientFactory(ReconnectingClientFactory):
    def startedConnecting(self, connector):
        print 'Started to connect.'

    def buildProtocol(self, addr):
        print 'Connected.'
        print 'Resetting reconnection delay'
        self.resetDelay()
        return Echo()

    def clientConnectionLost(self, connector, reason):
        print 'Lost connection. Reason:', reason
        ReconnectingClientFactory.clientConnectionLost(self, connector, reason)

    def clientConnectionFailed(self, connector, reason):
        print 'Connection failed. Reason:', reason
        ReconnectingClientFactory.clientConnectionFailed(self, connector,reason)
