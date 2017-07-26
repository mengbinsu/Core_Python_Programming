#!/usr/bin/env python
a = int(raw_input('enter a number:'))
b = int(raw_input('enter a number:'))
c = int(raw_input('enter a number:'))

if a < b:
    if a < c:
        print a,
        if (b < c):
            print b,c
        else:
            print c,b
    else:
        print c,a,b
elif a > b:
    if b > c:
        print c,b,a
    elif b < c:
        if a > c:
            print b,c,a
        else:
            print b,a,c
