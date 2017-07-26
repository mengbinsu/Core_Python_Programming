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

while True:
    num = int(raw_input('input a number:'))
    print isprime(num)
