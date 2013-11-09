#!/usr/bin/env  python
# -*-coding:utf-8 -*-
# Delaying Server - Chapter 5 - dalayserver.py
import socket
import traceback
import time

host = ''
port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)

while True:
    try:
        clientsock, clientaddr = s.accept()
    except KeyboardInterrupt:
        raise "-------"
    except:
        traceback.print_exc()
        continue

# Process the connection
try:
    print "Got connection from", clientsock.getpeername()
    while True:
        try:
            clientsock.sendall((time.asctime() + "\n"))
        except:
            break
        time.sleep(5)
except (KeyboardInterrupt, SystemExit):
    raise "****"
except:
    traceback.print_exc()

# Close the connection

try:
    clientsock.close()
except KeyboardInterrupt:
    raise "傻逼!"
except:
    traceback.print_exc()
