"""
Logging starts once log.startLogging has been called. After that, information can be
logged with log.msg or log.err ; use log.msg to log strings and use log.err to log
exceptions and failures . The default logging format produces output like this log of
the echo server starting up, echoing one message, and terminating:

"""

from twisted.internet import protocol, reactor
from twisted.python import log
class Echo(protocol.Protocol):
    def dataReceived(self, data):
        log.msg(data)
        self.transport.write(data)

class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()

log.startLogging(open('echo.log', 'w'))
reactor.listenTCP(8000, EchoFactory())
reactor.run()