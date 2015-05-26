"""
The Reactor
untuk server TCP = reactor.listenTCP(8000, Class Factory())
untuk client TCP = reactor.connectTCP("localhost", 8000, EchoFactory())

Protocol Factories
A new instance of our Echo protocol class is instantiated for every connection and goes
away when the connection terminates. This means that persistent configuration infor‐
mation is not saved in the protocol.
Persistent configuration information is instead kept in an EchoFactory class, which
inherits from protocol.Factory in the server and protocol.ClientFactory in the
client. 
- buildProtocol() 
  method creates a protocol for each new connection, which gets passed to the reactor to register callbacks.

A transport represents the connection between two endpoints communicating over a
network. Transports describe connection details: for example, is this connection stream-
oriented (like TCP) or datagram-oriented (like UDP)? TCP, UDP, Unix sockets, and
serial ports are examples of transports. Transports implement the ITransport interface,
which has the following methods:
- write
  Write data to the physical connection in a nonblocking manner.
- writeSequence
  Write a list of strings to the physical connection. Useful when working with line oriented protocols.
- loseConnection
  Write all pending data and then close the connection.
- getPeer
  Get the remote address of the connection.
- getHost
  Like getPeer , but returns the address of the local side of the connection.


methods:
- makeConnection
  Create a connection between two endpoints across a transport.
- connectionMade
  Called when a connection to another endpoint is made.
- dataReceived
  Called when data is received across a transport.
- connectionLost
  Called when the connection is shut down.
- basic.LineReceiver
  we don’t have to write our own boilerplate code for handling newline-delimited protocols
  
  
Tips mudah:
1. Define a protocol class, subclassing twisted.internet.protocol.Protocol for
arbitrary data or twisted.protocols.basic.LineReceiver for line-oriented pro‐
tocols.
2. Define a factory class, subclassing twisted.internet.protocol.Factory for
servers and twisted.internet.protocol.ClientFactory for clients. That factory
creates instances of the protocol and stores state shared across protocol instances.
3. Clients use reactor.connectTCP to initiate a connection to a server. Invoking
connectTCP registers callbacks with the reactor to notify your protocol when new
data has arrived across a socket for processing. Servers use reactor.listenTCP to
listen for and respond to client connections.
4. Communication doesn’t start until reactor.run is called, which starts the reactor
event loop.

"""