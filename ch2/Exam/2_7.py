#!/usr/bin/env python
InputStr = raw_input('Enter:')
for item in InputStr:
    print item
print

count = 0
while count < len(InputStr):
    print InputStr[count:count+1]
    count += 1
print
