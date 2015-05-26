from twisted.application import internet, service
from _01_echo import EchoFactory
application = service.Application("echo")
echoService = internet.TCPServer(8000, EchoFactory())
echoService.setServiceParent(application)