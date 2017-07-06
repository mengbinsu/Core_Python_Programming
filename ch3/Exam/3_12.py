#!/usr/bin/env python
'Create text file and read text file display'

import os
ls = os.linesep

def writeFile():
    'create text file'
    fname = raw_input('Enter a filename:')
    while True:
        if os.path.exists(fname):
            print "Error:%s already exists" %fname
        else:
            break;

    all = []
    print "\nEnter lines('.' by itself to quit).\n"

    while True:
        entry = raw_input('>')
        if entry == '.':
            break;
        else:
            all.append(entry)

    fobj = open(fname, 'w')
    fobj.writelines(['%s%s' %(x, ls) for x in all])
    fobj.close()
    print 'DONE'

def readFile():
    'read and display'
    fname  = raw_input('Enter filename:')
    print

    try:
        fobj = open(fname, 'r')
    except IOError, e:
        print "*** file open error:",e
    else:
        for eachLine in fobj:
            print eachLine,
        fobj.close()

while True:
    inputStr = raw_input('r:read file | w:write file | q:exit: ')
    if inputStr == 'r':
        readFile()
    elif inputStr == 'w':
        writeFile()
    elif inputStr == 'q':
        break;
print 'Bye'

