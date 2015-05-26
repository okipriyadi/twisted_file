"""
from twisted.internet import protocol, reactor
class Echo(protocol.Protocol):
    def dataReceived(self, data):
        self.transport.write(data)

class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()

reactor.listenTCP(8000, EchoFactory())
reactor.run()

To turn our echo server into an echo application, we can follow a simple algorithm:
1. Move the Protocol and Factory for the service into their own module.
2. Inside a TAC file:
    a. Create an instance of twisted.application.service.Application .
    b. Instead of registering the Protocol Factory with a reactor, like in Chapter 2,
    register the factory with a service, and register that service with the
    Application .


In our case, this means creating an instance of the TCPServer service, which will use
our EchoFactory to create instances of the Echo protocol on port 8000.

The code for managing the reactor will     be taken care of by twistd, which we'll discuss
next. The application code is now split into two files: echo.py, shown in Example 6-2;
and echo_server.tac, shown in Example 6-3.
Example 6-2. echo.py, a module containing the Protocol and Factory definitions


"""
#file echo.py ini
from twisted.internet import protocol, reactor

class Echo(protocol.Protocol):
    def dataReceived(self, data):
        self.transport.write(data)

class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()
