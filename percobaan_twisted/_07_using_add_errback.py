from twisted.internet.defer import Deferred
from twisted.python.failure import Failure
def myErrback(failure):
    print failure

d = Deferred()
d.addErrback(myErrback)
d.errback(Failure(Exception("Triggering errback.")))

"""
creates a Deferred d and uses its addErrback method to register the function 
myErrback with the errback chain. d.errback "fires" d and invokes the first function
in the errback chain, which only contains myErrback. The argument passed to err
"""