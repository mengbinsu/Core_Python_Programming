#!/usr/bin/env python
'read text file,display,edit'

import os

lineSum = 0;
allContent = []

while True:
    fname = raw_input('Enter filename:')
    print

    try:
        fobj = open(fname, 'r')
    except IOError, e:
        print "***file open error:", e
    else:
        for eachLine in fobj:
            print '%d' %lineSum, eachLine
            allContent.append(eachLine)
            lineSum += 1
        fobj.close()
        break

def getNewConten():
    while True:
        chooseLineNum = raw_input('Enter a line number which do you want to edit [0, %d]' %lineSum)
        try:
            chooseLineNum = int(chooseLineNum)
            if not (0 <= chooseLineNum < lineSum):
                print '>>>[ERROR] line number must in [0-%d]' %lineSum
                continue
            break
        except ValueError, e:
            print '>>>[ERROR] number transform failed: ', e

    print '>>> your choose line is :%d' %chooseLineNum
    newContent = raw_input('>>>input new content: ')
    allContent[chooseLineNum] = newContent + os.linesep

if lineSum > 0:
    getNewConten()
else:
    print '>>>file is empty, please input new content '
    newContent = raw_input('>>>')
    allContent.append(newContent)

fobj = open(fname, 'w')
for line in allContent:
    fobj.write(line)
fobj.close()
print '>>>save success.'

print '***display file after modified***'
fobj = open(fname, 'r')
for eachLine in fobj:
    print eachLine
fobj.close()
