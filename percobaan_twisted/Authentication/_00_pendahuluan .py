"""
Twisted comes with a protocol-independent, pluggable, asynchronous authentication
system called Cred that can be used to add any type of authentication support to your
Twisted server.

Before we get into the usage examples, there are a few terms that you should familiarize
yourself with:

- Credentials
  Information used to identify and authenticate a user. Common credentials are a
  username and password, but they can be any data or object used to prove a user’s
  identity, such as a certificate or challenge/response protocol. Objects that provide
  credentials implement twisted.cred.credentials.ICredentials .
- Avatar
  A business logic object in a server application that represents the actions and data
  available to a user. For example, an avatar for a mail server might be a mailbox
  object, an avatar for a web server might be a resource, and an avatar for an SSH
  server might be a remote shell.
  Avatars implement an interface that inherits from zope.interface.Interface .
- Avatar ID
  A string returned by the credentials checker that identifies the avatar for a user. This
  is often a username, but it could be any unique identifier. Example avatar IDs are
  “Joe Smith”, “joe@localhost”, and “user926344”.
- Credentials checker
  An object that takes credentials and attempts to verify them. The credentials checker
  is the bridge between the many ways credentials can be stored—for example, in a
  database, in a file, or in memory—and the rest of Cred.
  If the credentials correctly identify a user, the credentials checker will return an
  avatar ID. Credentials checkers can also support anonymous access by returning
  twisted.cred.checkers.ANONYMOUS .
  Credentials checkers implement the twisted.cred.checker.ICredentialsChecker interface.  
- Realm
  An object that provides access to all the possible avatars in an application. A realm
  will take an avatar ID identifying a specific user and return an avatar object that
  will work on behalf of that user. A realm can support multiple types of avatars,
  allowing different types of users to have access to different services on a server.
  Realm objects implement the twisted.cred.portal.IRealm interface.
- Portal
  The portal mediates interactions between the many parts of Cred. At the protocol
  level, the only thing you need to use Cred is a reference to a portal. The portal’s
  login method will authenticate users to the system.
  The portal is not subclassed. Customization instead happens in the realm, 
  credentials checkers, and avatars.
"""