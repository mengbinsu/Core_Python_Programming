#!/usr/bin/env python

import string
import keyword

alphas = string.letters + '_'
nums = string.digits

print 'Welcome to the Identifier Checker v1.0'
print 'Testees must be at least 2 chars long.'
myInput = raw_input('Identifier to test? ')

if myInput[0] not in alphas:
    print 'invalid: first symbol must be alphabetic'
else:
    if len(myInput) == 0:
        print 'okay as an identifier'
    else:
        for otherChar in myInput[1:]:
            if otherChar not in alphas + nums:
                print 'invalid:remaining symbols must be alphabetic '
                break;
        if keyword.iskeyword(myInput):
            print 'invalid:input string is a keyword'
        else:
            print 'okay as an identifier'
