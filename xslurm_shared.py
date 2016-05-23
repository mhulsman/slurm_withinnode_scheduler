import xmlrpclib
import httplib
import socket
from dns import resolver, reversename

class TimeoutHTTPConnection(httplib.HTTPConnection):
    def __init__(self,host,timeout=10):
        httplib.HTTPConnection.__init__(self, host, timeout = timeout)

class TimeoutTransport(xmlrpclib.Transport):
    def __init__(self, timeout = 10, *l, **kw):
        xmlrpclib.Transport.__init__(self, *l, **kw)
        self.timeout = timeout

    def make_connection(self, host):
        conn = TimeoutHTTPConnection(host, self.timeout)
        return conn

class TimeoutServerProxy(xmlrpclib.ServerProxy):
    def __init__(self, uri, timeout = 10, *l, **kw):
        kw['transport'] = TimeoutTransport(timeout = timeout, use_datetime = kw.get('use_datetime', 0))
        xmlrpclib.ServerProxy.__init__(self, uri, *l, **kw)

#self register
port = 38763
address = 'localhost'
job_url = 'http://' + address + ':' + str(port + 1)

def get_hostname():
    #get IP address
    socket.setdefaulttimeout(30)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM); 
    s.connect(('google.com', 0)); 
    myip = s.getsockname()[0]

    try:
        addr=reversename.from_address(myip)
        myip = str(resolver.query(addr,"PTR")[0])[:-1]
    except Exception,e:
        pass

    return myip

