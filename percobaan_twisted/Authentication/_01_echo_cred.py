from zope.interface import implements, Interface
from twisted.cred import checkers, credentials, portal
from twisted.internet import protocol, reactor
from twisted.protocols import basic

class IProtocolAvatar(Interface):
    def logout():
        """
        Clean up per-login resources allocated to this avatar.
        """

class EchoAvatar(object):
    implements(IProtocolAvatar)
    
    def logout(self):
        pass

class Echo(basic.LineReceiver):
    portal = None
    avatar = None
    logout = None
    
    def connectionLost(self, reason):
        if self.logout:
            self.logout()
            self.avatar = None
            self.logout = None
        
    def lineReceived(self, line):
        if not self.avatar:
            username, password = line.strip().split(" ")
            self.tryLogin(username, password)
        else:
            self.sendLine(line)

    def tryLogin(self, username, password):
        self.portal.login(credentials.UsernamePassword(username,
                                                       password),
                          None,
                          IProtocolAvatar).addCallbacks(self._cbLogin,self._ebLogin)
                          
    def _cbLogin(self, (interface, avatar, logout)):
        self.avatar = avatar
        self.logout = logout
        self.sendLine("Login successful, please proceed.")

    def _ebLogin(self, failure):
        self.sendLine("Login denied, goodbye.")
        self.transport.loseConnection()
    
class EchoFactory(protocol.Factory):
    def __init__(self, portal):
        self.portal = portal
    def buildProtocol(self, addr):
        proto = Echo()
        proto.portal = self.portal
        return proto

class Realm(object):
    implements(portal.IRealm)
    def requestAvatar(self, avatarId, mind, *interfaces):
        if IProtocolAvatar in interfaces:
            avatar = EchoAvatar()
            return IProtocolAvatar, avatar, avatar.logout
        raise NotImplementedError("This realm only supports the IProtocolAvatar interface.")

realm = Realm()
myPortal = portal.Portal(realm)
checker = checkers.InMemoryUsernamePasswordDatabaseDontUse()
checker.addUser("user", "pass")
myPortal.registerChecker(checker)
reactor.listenTCP(8001, EchoFactory(myPortal))
reactor.run() 

"""
The steps are:
1. Our protocol factory, EchoFactory , produces instances of Echo in its
buildProtocol method, just like in Chapter 2. Unlike in Chapter 2, these protocols
have a reference to a Portal .
When we receive our first line from a connected client in Echo.lineReceived , we
call our Portal ’s login method to initiate a login request. Portal.login ’s function
signature is login(credentials, mind, *interfaces) . In detail, the three argu‐
ments it requires are:
a. Credentials, in this case a credentials.UsernamePassword created from the
username and password parsed out of the line received.
b. A “mind” which is almost always None . We won’t ever care about the mind in
this book; if you are curious, the Portal.login documentation explains it.
c. A list of avatar interfaces for which we are requesting authentication. This is
usually a single interface (in this example, IProtocolAvatar ).
2. The Portal hands off the credentials to the appropriate credentials checker based
on the avatar interface requested.
Each credentials checker exposes a set of credentialInterfaces for which it is
able to authenticate. This example has only one checker, a toy checkers.InMemo
ryUsernamePasswordDatabaseDontUse that Twisted provides for learning
about cred . This checker happens to support two types of credentials,
credentials.IUsernamePassword and credentials.IUsernameHashedPassword .
Because the call to Portal.login specified credentials.UsernamePassword ,
"""