#!/usr/bin/env python
import string

alphas = string.letters + '_'
nums = string.digits

print 'Welcome to the Identifier Checker V1.0'
print 'Testrees must be at least 2 chars long.'

myInput = raw_input('Identifier to test? ')
if len(myInput) > 1:

    if myInput[0] not in alphas:
        print '''invalid: first symbol must be
              alphabetic'''

    else:
        for otherChar in myInput[1:]:

            if otherChar not in alphas + nums:
                print '''invalid: remaining symbol must be
			alphabetic'''

                break
            else:
                print "okay as an Identifier"
