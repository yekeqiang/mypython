#!/usr/bin/env python
# Echo Server woth Threading
# Compare to echo server in

import socket
import traceback
import os
import sys
from threading import *
host = ''
port = 51423


def handlechild(clientsock):
    print "New child", currentThread().getName()
    print "Got connection from", clientsock.getpeername()
    while True:
        data = clientsock.recv(4096)
        if not len(data):
            break
        clientsock.sendall(data)

    # Close the connection
    clientsock.close()

# Set up the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SOREUSEADDR, 1)
s.bind((host, port))
s.listen(1)

while True:
    try:
        clientsock, clientaddr = s.accept()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
        continue
t = Thread(target=handlechild, args=[clientsock])
t.setDaemon(1)
t.start()
