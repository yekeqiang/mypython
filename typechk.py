#!/usr/bin/env python


def displayNumType(num):
    print num, 'is'
    if isinstance(num, (int, long, float, complex)):
        print 'a number of type:', type(num).__name__
    else:
        print 'not a number at all!!!'

isplayNumType(-69)
displayNumType(999999999999999999999999999)
displayNumType(98.6)
displayNumType(-5.2 + 1.9j)
displayNumType('xxxx')
