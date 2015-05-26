"""
As always, we register a factory that generates instances of our protocol with the reactor.
In this case, instead of subclassing protocol.Protocol directly, we are taking advantage
of a higher-level API, http.HTTPChannel , which inherits from basic.LineReceiver
and already understands the structure of an HTTP request and the numerous behaviors
required by the HTTP RFCs

Our MyHTTP protocol specifies how to process requests by setting its requestFactory
instance variable to MyRequestHander , which subclasses http.Request


"""
from twisted.internet import reactor
from twisted.web import http
class MyRequestHandler(http.Request):
    resources = {
                 '/': '<h1>Home</h1>Home page',
                 '/about': '<h1>About</h1>All about me',
                 }
    
    def process(self):
        self.setHeader('Content-Type', 'text/html')
        if self.resources.has_key(self.path):
            self.write(self.resources[self.path])
        else:
            self.setResponseCode(http.NOT_FOUND) # setRespondCode memberikan code 200 jika resource tersedia dan #http.NOT_FOUND = send a 404, page not found 
            self.write("<h1>Not Found</h1>Sorry, no such resource.")
        self.finish()
        
class MyHTTP(http.HTTPChannel):
    requestFactory = MyRequestHandler

class MyHTTPFactory(http.HTTPFactory):
    def buildProtocol(self, addr):
        return MyHTTP()

reactor.listenTCP(8000, MyHTTPFactory())
reactor.run()
            