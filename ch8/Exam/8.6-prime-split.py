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

def prime_split(num):
    if num <= 1:
        return []
    if isprime(num):
        return [num]

    factors = getfactors(num)
    if len(factors) > 2:
        result = []
        maxF = factors[-2]
        tmp = divmod(num, maxF)

        result += prime_split(maxF)
        result += prime_split(tmp[0])

        return sorted(result)
    else:
        return []

while True:
    print prime_split(int(raw_input('input a number:')))
