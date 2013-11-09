#!/usr/bin/env python
# SimpleXMLRPCServer Example with extra class features
# stat.py
# This program requires Python 2.3 or above

# from SimpleXMLRPCServer import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler
from DocXMLRPCServer import DocXMLRPCServer, DocCGIXMLRPCRequestHandler
from SocketServer import ThreadingMixIn
import time


class Stats:

    def getstats(self):
        """Returns a dictionary, The keys are names of the functions.
        and the values are the  number of times each function was called."""

        return self.callstats

    def getruntime(self):
        """Returns the number of seconds the class has been instantiated"""
        return time.time() - self.starttime

    def failure(self):
        """Causes a RuntimeError to be raised"""
        raise RuntimeError("This function always raises an error.")


class Math(Stats):

    def __init__(self):
        self.callstats = {'pow': 0, 'hex': 0}
        self.starttime = time.time()

    def pow(self, x, y):
        """Returns x raised to the yth power; that is,x ^ y.
        x and y may be integers or floating-point values."""

        self.callstats['pow'] += 1  # Doesn't do what you expect
        return pow(x, y)

    def hex(self, x):
        """Returns a string holding a hexadecimal representation of
        the integer x."""
        self.callstats['hex'] += 1
        return "%x" % x


# class ForkingServer(ThreadingMixIn, SimpleXMLRPCServer):
    # pass
class ThreadingServer(ThreadingMixIn, DocXMLRPCServer):
    pass

serveraddr = ('', 8765)
srvr = ThreadingServer(serveraddr, DocCGIXMLRPCRequestHandler)
srvr.set_server_title("Chapter 19 Example Documetation")
srvr.set_server_name("Chapter 18 Doc")
srvr.set_server_documentation(
    """Welcome to the sample DocXMLRPCServer from Chapter 18.""")
srvr.register_instance(Math())
srvr.register_introspection_functions()
srvr.serve_forever()


# srvr = ForkingServer(serveraddr, SimpleXMLRPCRequestHandler)
# srvr.register_instance(Math())
# srvr.register_introspection_functions()
# srvr.serve_forever()
