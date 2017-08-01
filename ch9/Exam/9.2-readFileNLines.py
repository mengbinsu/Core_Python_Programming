#!/usr/bin/env python

fileName = raw_input('FileName: ')
num = int(raw_input('Display First N lines: '))

readLine = 0
f = open(fileName)
for eachLine in f:
    if readLine == num:
        break;
    print eachLine,
    readLine += 1
f.close()

