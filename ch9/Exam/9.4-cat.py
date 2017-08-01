#!/usr/bin/env python

fileName = raw_input('FileName: ')
lineNum = 0
f = open(fileName)
for eachLine in f:
    if lineNum % 2 == 0 and lineNum > 0:
        if(len(raw_input('Enter any key to continue...'))):
            continue
    lineNum += 1
    print '%2d ' %lineNum, eachLine
f.close()
