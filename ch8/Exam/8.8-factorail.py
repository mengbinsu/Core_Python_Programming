#!/usr/bin/env python

def factorial(N):
    if N <= 0:
        return None
    return reduce(lambda x, y:x * y, range(1, N+1))

while True:
    print factorial(int(raw_input('input a number: ')))
