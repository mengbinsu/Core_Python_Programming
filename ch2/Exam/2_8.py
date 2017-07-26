#!/usr/bin/env python
subtot = 0
for i in range(5):
    subtot += int(raw_input('enter a number: '))
print subtot

print sum(int(raw_input('enter a number:')) for i in range(5) )
