#!/usr/bin/env python
# Simple Gopher Client with basic error handling - Chapter 1
# gopherclient2.py
import socket
import sys

port = 70
host = sys.argv[1]
filename = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
fd = s.makefile('rw', 0)

fd.write(filename + '\r\n')

for line in fd.readline():
    sys.stdout.write(line)
