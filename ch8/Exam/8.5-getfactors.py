#t!/usr/bin/env python
import math
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

while True:
    num = int(raw_input('input a number:'))
    print getfactors(num)
