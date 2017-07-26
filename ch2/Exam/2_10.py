#!/usr/bin/env python
while True:
    if 0 < int(raw_input('Enter a number in range(0, 100):')) < 100:
        print 'Exit'
        break;
    else:
        print 'Input error, try again'
