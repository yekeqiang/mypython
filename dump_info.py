#!/usr/bin/env python
# Obtain Web Page Information
import sys
import urllib2

req = urllib2.Request(sys.argv[1])
# req = urllib2.
fd = urllib2.urlopen(req)
print "Retrieved", fd.geturl()
info = fd.info()
for key, value in info.items():
    print "%s = %s" % (key, value)
