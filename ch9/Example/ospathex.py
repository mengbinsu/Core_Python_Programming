#!/usr/bin/env python

import os
for tmpdir in ('/tmp', r'c:\temp'):
    if os.path.isdir(tmpdir):
        break;
else:
    print 'no temp dirctory available'
    tmpdir = ''

if tmpdir:
    os.chdir(tmpdir)
    cwd = os.getcwd()
    print '***current temporary directory'
    print cwd

    print '***creating example directroy'
    os.mkdir('example')
    os.chdir('example')
    cwd = os.getcwd()
    print '***new workding dirctory'
    print os.listdir(cwd)
    print '*** creating test file ...'
    fobj = open('test', 'w')
    fobj.write('foo\n')
    fobj.write('foo\n')
    fobj.write('foo\n')
    fobj.write('foo\n')
    fobj.close()
    print '***updated directory listing:'
    print os.listdir(cwd)

    print "*** renaming 'test' to 'filetest.txt'"
    os.rename('test', 'filetest.txt')
    print '*** updated dirctory listing'
    print os.listdir(cwd)

    path = os.path.join(cwd, os.listdir(cwd)[0])
    print '***full file pathname'
    print path
    print '***(filename, extension) =='
    print os.path.splitext(os.path.basename(path))

    print '***displaying file content'
    fobj = open(path)
    for eachLine in fobj:
        print eachLine,
    fobj.close()

    print '***deleting test file'
    os.remove(path)
    print '***updated directory listing: '
    print os.listdir(cwd)
    os.chdir(os.pardir)
    print '***deleting test dirctory'
    os.rmdir('example')
    print '***DONE'

