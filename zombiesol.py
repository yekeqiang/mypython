#!/usr/bin/env python
# Zombie problem solution

import os
import time
import signal


def childhandler(signum, stackframe):
    """Signal handler. Runs on the parent and is called whenever
    a child terminates."""

    while True:
        # Repeat as long as there are children to collect
        try:
            result = os.waitpid(-1, os.WHOHANG)
        except:
            break
        print "Reaped child process %d" % result[0]

        # Reset the signal handler so future signals trigger this function
        signal.signal(signal.SIGCHLD, childhandler)

# INstall signal handler so that childhandler() gets called whenever
# child process terminates
# signal.signal(signal.SIGCHLD, childhadnler)
signal.signal(signal.SIGCHLD, childhandler)

print "Before the fork, my PID is", os.getpid()

pid = os.fork()
if pid:
    print "Hello from the parent, The child will be PID %d" % pid
    print "Sleeping 10 seconds..."
    time.sleep(20)
    print "Sleep done"
else:
    print "Child sleeping 5 seconds..."
    time.sleep(5)
