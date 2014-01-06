#!/usr/bin/env python
# Threading with semaphores
import threading
import time
import random


def numbergen(sem, queue, qlock):
    while True:
        time.sleep(2)   # Simulate a complex I/O load
        if random.randint(0, 1):
            # Generate something half the time
            value = random.randint(0, 100)
            qlock.acquire()
            try:
                queue.append(value)
            finally:
                qlock.release()
            print "Placed %d on the queue." % value

            sem.release()


def numbercalc(sem, queue, qlock):
    while True:
        sem.acquire()
        qlock.acquire()
        try:
            value = queue.pop(0)
        finally:
            qlock.release()
        print "%s: Got %d from the queue." % \
            (threading.currentThread().getName(), value)
        newvalue = value * 2

        time.sleep(3)  # Simulate a complex calculation

childthreads = []

sem = threading.Semaphore(0)
queue = []
qlock = threading.Lock()
# Create the number generator
t = threading.Thread(target=numbergen, args=[sem, queue, qlock])
t.setDaemon(1)
t.start()
childthreads.append(t)

# Create the two threads that work with the numbers
for i in range(1, 3):
    t = threading.Thread(target=numbercalc, agrs=[sem, queue, qlock])
    t.setDaemon(1)
    t.start()
    childthreads.append(t)
while True:
    # Sleep forever
    time.sleep(300)
