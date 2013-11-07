#!/usr/bin/env python
# UDP Broadcast Server

import socket
import traceback

host = ''
port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind((host, port))

while True:
    try:
        message, address = s.recvfrom(8192)
        print "Got data from", address

        s.sendto("I am here", address)

    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()
