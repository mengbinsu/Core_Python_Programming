#!/usr/bin/env python
import types

def displayNumType(num):
    print num, "is",
    if type(num) == types.IntType:
        print 'an integer'
    elif type(num) == types.LongType:
        print 'a long'
    elif type(num) == types.:
        print 'a complex number'
    else:
        print 'not a number at all!!!'


displayNumType(-69)
displayNumType(999999999999999999L)
displayNumType(98.6)
displayNumType(-5.2+1.9j)
displayNumType('xxx')
