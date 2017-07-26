#!/usr/bin/env python

while True:
    f = raw_input('(f)rom:')
    t = raw_input('(t)o:')
    i = raw_input('(i)ncrement:')

    print range(int(f), int(t), int(i))
