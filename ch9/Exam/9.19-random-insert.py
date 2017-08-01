#!/usr/bin/env python

from random import randint

def create(filenmae, value, total, maxlen):
    assert 0 <= value <= 255
    ls = [chr(randint(0, 255)) for i in xrange(maxlen - total)]
    ch = chr(value)
    for i in xrange(total - ls.count(ch)):
        ls.insert(randint(0, len(ls) - 1), ch)
    for i in xrange(maxlen - len(ls)):
        ls.insert(randint(0, len(ls)-1), chr(randint(0, value - 1)))
    with open(filename, 'wb') as f:
        f.write(''.join(ls))

if __name__ == '__main__':
    filename = raw_input('filename: ')
    value = int(raw_input('value: '))
    total = int(raw_input('total: '))
    maxlen = int(raw_input('max length of file: '))
    create(filename, value, total, maxlen)
