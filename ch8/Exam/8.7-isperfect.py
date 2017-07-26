#!/usr/bin/env python
import math

def isprime(num):
    count = int(math.sqrt(num))
    while count > 1:
        if num % count == 0:
            return False
        count -= 1
    else:
        return True

def getfactors(num):
    if num <= 0:
        return []

    result = set([])
    count = int(math.sqrt(num))
    while count > 0:
        tmp = divmod(num, count)
        if tmp[1] == 0:
            result.add(count)
            result.add(tmp[0])
        count -= 1

    return sorted([x for x in result])

def isperfect(num):
    factors = getfactors(num)
    return sum(factors) - num == num

while True:
    print isperfect(int(raw_input('input a number: ')))


