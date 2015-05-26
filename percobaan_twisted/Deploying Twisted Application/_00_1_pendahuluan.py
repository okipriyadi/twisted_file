"""
SERVICES
A service is anything that can be started and stopped and that implements the IService
interface. Twisted comes with service implementations for TCP, FTP, HTTP, SSH, DNS,
and many other protocols. Many services can register with a single application.

The core of the IService interface is:
- startService
  Start the service. This might include loading configuration data, setting up database
  connections, or listening on a port.
- stopService
  Shut down the service. This might include saving state to disk, closing database
  connections, or stopping listening on a port.
  Our echo service uses TCP, so we can use Twisted’s default TCPServer implementation
  of this IService interface.

APPLICATIONS 
An application is the top-level container for one or more services that are deployed
together. Services register themselves with an application, and the twistd deployment
utility described shortly searches for and runs applications.
We’ll create an echo application with which the echo service can register.

TAC FILES
When writing a Twisted program as a regular Python file, the developer is responsible
for writing code to start and stop the reactor and to configure the program. Under the
Twisted application infrastructure, protocol implementations live in a module, services
using those protocols are registered in a Twisted application configuration (TAC) file,
and the reactor and configuration are managed by an external utility.



"""