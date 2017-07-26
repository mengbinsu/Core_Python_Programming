#!/usr/bin/env python
subtot = 0
for i in range(5):
    subtot += int(raw_input('enter a number: '))
print '%f' %(float(subtot)/5)

print '%f' %(float(sum(int(raw_input('enter a number:')) for i in range(5)))/5)
