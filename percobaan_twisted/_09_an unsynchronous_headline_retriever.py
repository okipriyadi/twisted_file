"""
uses a helpful reactor method called callLater , which you can use to
schedule events. In this example, we use callLater in getHeadline to fake an asynchronous 
event arriving after one second.
"""
from twisted.internet import reactor, defer
from twisted.python.failure import Failure

class HeadlineRetriever(object):
    def processHeadline(self, headline):
        if len(headline) > 50:
            self.d.errback(Failure(Exception("The headline ``%s'' is too long!" % (headline,))))
        else:
            self.d.callback(headline)

    def _toHTML(self, result):
        return "<h1>%s</h1>" % (result,)

    def getHeadline(self, input):
        self.d = defer.Deferred()
        reactor.callLater(1, self.processHeadline, input)
        self.d.addCallback(self._toHTML)
        return self.d
    
def printData(result):
    print result
    reactor.stop()

def printError(failure):
    print failure
    reactor.stop()
    
h = HeadlineRetriever()
d = h.getHeadline("Breaking News: Twisted Takes Us to the Moon xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx!")
d.addCallbacks(printData, printError)
reactor.run()