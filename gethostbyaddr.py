#!/usr/bin/env python
# Basic gethostbyaddr() example
# This program performs a reverse lookup on the address
# on the command line

import sys
import socket

try:
    # Perform the lookup
    result = socket.gethostbyaddr(sys.argv[1])

    # Display the looked-up hostname
    print "Primary hostname:"
    print " " + result[0]

    # Display the list of available addresses that is also returned
    print "\nAddresses:"
    for item in result[2]:
        print " " + item
except socket.herror as e:
    print "Couldn't look up name:", e
