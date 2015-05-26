"""
What if we wanted to store our passwords in a database?
Twisted does not ship with a database-backed credentials checker, so we’ll need to write
our own. It must implement the ICredentialsChecker interface, namely:
• Expose a class variable credentialInterfaces , which lists the credentials types the
checker is able to check
• Implement the requestAvatarId method, which, given a set of credentials, must
either authenticate the user and return its avatar ID or return a login failure
"""

from twisted.cred import error
from twisted.cred.checkers import ICredentialsChecker
from twisted.cred.credentials import IUsernameHashedPassword
from twisted.internet.defer import Deferred
from zope.interface import implements

class DBCredentialsChecker(object):
    implements(ICredentialsChecker)
    credentialInterfaces = (IUsernameHashedPassword,)
    
    def __init__(self, runQuery, query):
        self.runQuery = runQuery
        self.query = query

    def requestAvatarId(self, credentials):
        for interface in self.credentialInterfaces:
            if interface.providedBy(credentials):
                break
            else:
                raise error.UnhandledCredentials()

        dbDeferred = self.runQuery(self.query, (credentials.username,))
        deferred = Deferred()
        dbDeferred.addCallbacks(self._cbAuthenticate, self._ebAuthenticate,
        callbackArgs=(credentials, deferred),
        errbackArgs=(credentials, deferred))
        return deferred
    def _cbAuthenticate(self, result, credentials, deferred):
        if not result:
            deferred.errback(error.UnauthorizedLogin('User not in database'))
        else:
            username, password = result[0]
            if credentials.checkPassword(password):
                deferred.callback(credentials.username)
            else:
                deferred.errback(error.UnauthorizedLogin('Password mismatch'))
    
    def _ebAuthenticate(self, failure, credentials, deferred):
        deferred.errback(error.LoginFailed(failure))