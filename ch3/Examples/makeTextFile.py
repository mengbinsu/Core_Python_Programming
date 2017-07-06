#!/usr/bin/env python
'makeTextFile.py -- create text file'

import os
ls = os.linesep
fname = raw_input('Enter a filename:')

while True:
    if os.path.exists(fname):
        print "ERROR:'%s' already exists" % fname
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
fobj.writelines(['%s%s' % (x, ls) for x in all])
fobj.close()
print 'DONE!'

