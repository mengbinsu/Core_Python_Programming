#!/usr/bin/env python
InputStr = raw_input('Enter numbers:')
while InputStr != 'End':
    InputDigit = int(InputStr)
    if InputDigit < 0 :
        print 'less than zero'
    elif InputDigit > 0:
        print 'more than zero'
    else:
        print 'equal zero'
    InputStr = raw_input('Enter numbers:')
print 'Game Over'
