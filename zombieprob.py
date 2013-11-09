#!/usr/bin/env python
# Zombie problem demnstration
import os
import time

print "Before the fork, my PID is", os.getpid()

pid = os.fork()
if pid:
    print "Hello from the parent. The child will be be PID %d" % pid
    print "Sleeoping 120 seconds..."
    time.sleep(120)
