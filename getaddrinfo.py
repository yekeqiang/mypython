#!/usr/bin/env python
# Basic getaddrinfo() basic example

import sys
import socket

result = socket.getaddrinfo(sys.argv[1], None)
print result[0][4]
