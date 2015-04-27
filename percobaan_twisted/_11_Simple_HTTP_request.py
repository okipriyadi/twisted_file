"""
As with our basic TCP servers from Chapter 2, we create a protocol factory,
HTTPEchoFactory , inheriting from protocol.ServerFactory . It builds instances of our
HTTPEchoProtocol , which inherits from basic.LineReceiver so we don't have to write
our own boilerplate code for handling newline-delimited protocols.
We keep track of lines as they are received in lineReceived until we reach an empty
line, the carriage return and line feed ( \r\n ) marking the end of the headers sent by the
client. We then echo back the request text and terminate the connection.
HTTP uses TCP as its transport-layer protocol, so we use listenTCP to register callbacks
with the reactor to get notified when TCP packets containing our HTTP data arrive on
our designated port.
"""
from twisted.protocols import basic
from twisted.internet import protocol, reactor
class HTTPEchoProtocol(basic.LineReceiver):
    
    def __init__(self):
        self.lines = []
    
    def lineReceived(self, line):
        self.lines.append(line)
        if not line:
            self.sendResponse()

    def sendResponse(self):
        self.sendLine("HTTP/1.1 200 OK")
        self.sendLine("")
        responseBody = "You said:\r\n\r\n" + "\r\n".join(self.lines)
        self.transport.write(responseBody)
        self.transport.loseConnection()


class HTTPEchoFactory(protocol.ServerFactory):
    def buildProtocol(self, addr):
        return HTTPEchoProtocol()

reactor.listenTCP(8000, HTTPEchoFactory())
reactor.run()