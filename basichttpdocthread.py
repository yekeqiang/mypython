#!/usr/bin/env python
# Basic HTTP Server Example with Two Document
# basichttpdocthread.py

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn
import time
import threading

starttime = time.time()


class RequestHandler(BaseHTTPRequestHandler):

    """Definition of the request handler."""

    def _writeheaders(self, doc):
        """Write the HTTP headers for the document, If there's no
        document, send a 404 error code; otherwise, send a 200 success code."""

        if doc is None:
            message = "the page is not found"
            self.send_response(404, message)
        else:
            self.send_response(200)

        # Always serve up HTML for now.
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def _getdoc(self, filename):
        """Handle arequest for document, returning one of two
        different pages as appropriate"""

        global starttime
        if filename == '/':
            return """<html><head><title>Sample Page</title></head> \
    		<body>This is a sample page. You can also look at the \
    		<a href="stats.html">server statistics</a> \
    		</body></html>
    		"""
        elif filename == '/stats.html':
            return """<html><head><title>Statistics</head> \
    		<body>This server has been running for %d seconds. \
    		</body></html> """ % int(time.time() - starttime)
        else:
            return None
      #       return """<html><head><title>Statistics</head> \
    		# <body>This server has been running for %d seconds. \
    		# </body></html> """ % int(time.time() - starttime)

    def do_HEAD(self):
        """Handle a request for headers only"""
        doc = self._getdoc(self.path)
        self._writeheaders(doc)

    def do_GET(self):
        """Handle a request for headers and body"""
        print "Handling with thread", threading.currentThread().getName()
        doc = self._getdoc(self.path)
        self._writeheaders(doc)
        if doc is None:
            self.wfile.write("""<html><head><title>Not Found</title></head>
    			<body>The Request document '%s' was not found.</body>
    			</html>
    			""" % self.path)
        else:
            self.wfile.write(doc)


class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    pass


# Create the object and server requests

serveraddr = ('', 8765)
srvr = ThreadingHTTPServer(serveraddr, RequestHandler)
srvr.serve_forever()
