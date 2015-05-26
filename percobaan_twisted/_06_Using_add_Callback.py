"""
addCallback adalah methd untuk me-register fungsi callback
"""
from twisted.internet.defer import Deferred
def myCallback(result):
    print result

d = Deferred()
d.addCallback(myCallback)
d.callback("Triggering callback.")

"""
creates a Deferred d and uses its addCallback method to register the
function myCallback with the callback chain. d.callback "fires" d and invokes the
callback chain, which only contains myCallback . The argument passed to callback is
propagated as an argument to the first function in the callback chain.
"""