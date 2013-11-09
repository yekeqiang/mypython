#!/usr/bin/env python
# Echo Server with Forking
# Compare to echo server in

import socket
import traceback
import os
import sys


def reap():
    # Collect any child processes that may be outstanding
    while True:
        try:
            result = os.waitpid(-1, os.WNOHANG)
            if not result[0]:
                break
        except:
            break
        print "Reaped child process %d" % result[0]

host = ''
port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)

print "Parent at %d listening for connections" % os.getpid()

while True:
    try:
        clientsock, clientaddr = s.accept()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
        continue
        # Clean up old children
    reap()

        # Fork a process for this connection
    pid = os.fork()

    if pid:
            # This is the parent process. Close the child's socket
            # and return to the top of the loop
        clientsock.close()
        continue
    else:
            # From here on, this is the child
        s.close()   # Close the parent's socket

            # Process the connection
    try:
        print "Child from %s being handled by PID %d" % \
            (clientsock.getpeername(), os.getpid())
        while True:
            data = clientsock.recv(4096)
            if not len(data):
                break
            clientsock.sendall(data)
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()

    # Close the connection

    try:
        clientsock.close()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
    sys.exit(0)
