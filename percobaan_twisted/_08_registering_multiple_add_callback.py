from twisted.internet.defer import Deferred
def addBold(result):
    return "<b>%s</b>" % (result,)

def addItalic(result):
    return "<i>%s</i>" % (result,)

def printHTML(result):
    print result

d = Deferred()
d.addCallback(addBold)
d.addCallback(addItalic)
d.addCallback(printHTML)
d.callback("Hello World")
"""
Deferred s also sport an addCallbacks method, which registers both a callback and an
errback at the same level in their respective callback chains. For example:
d = Deferred()
d.addCallbacks(myCallback, myErrback)
d.callback("Triggering callback.")
"""