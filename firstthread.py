#!/usr/bin/env python
# First thread example
import threading
import time
import sys


def sleeppandprint():
    time.sleep(1)
    print "Hellp from both of us"


def threadcode():
    sys.stdout.write("Hello from the new thread. My name is %s\n" %
                     threading.currentThread().getName())
    sleeppandprint()

print "Before starting a new thread, my name is", \
    threading.currentThread().getName()

# Create new thread.
t = threading.Thread(target=threadcode, name="ChildThread")

# This thread won't keep the porgram from terminating
t.setDaemon(1)

# Start the new thread.
t.start()
sys.stdout.write(
    "Hello from the main thread. My name is %s\n" %
    threading.currentThread().getName())
sleeppandprint()

# Wait for the child thread to exit
t.join()
