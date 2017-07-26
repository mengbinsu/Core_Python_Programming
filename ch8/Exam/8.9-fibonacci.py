#!/usr/bin/env python

def fibonacci(N):
    if N <= 2:
        return 1

    tmp = [1, 1]
    for x in range(2, N):
        tmp.append(tmp[-2]+tmp[-1])

    return tmp[-1]

while True:
    print fibonacci(int(raw_input('input a number: ')))
