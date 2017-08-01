#!/usr/bin/env python

def counts(filename, value):
    ch = chr(value)
    with open(filename, 'rb') as f:
        total = sum(item.count(ch) for item in f)
    return total

if __name__ == '__main__':
    filename = raw_input('file name:')
    value = int(raw_input('value: '))
    print counts(filename, value)
