#!/usr/bin/env python
# Basic getaddrinfo() not quite rigjt list example
# Getaddrinfo-list-broken.py
# Takes a hostname on the command line and prints all result
# matches for it. Broken;a given name may occur
import sys
import socket

# Put the list of results into the "result" variable
result = socket.getaddrinfo(sys.argv[1], None, 0, socket.SOCK_STREAM)

counter = 0
for item in result:
    # Print out the address tuple for each item
    print "%-2d: %s" % (counter, item[4])
    counter += 1
