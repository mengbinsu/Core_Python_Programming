#!/usr/bin/env python

import os
import importlib
from warnings import catch_warnings

pymodules = {}
path = '/usr/local/lib/python2.7'
suffix = '.py'

pyfiles = [f for f in os.listdir(path) if f.endswith(suffix)]
for f in pyfiles:
    module_name = os.path.splitext(f)[0]
    try:
        module = importlib.import_module(module_name)
        pymodules[module_name] = module.__doc__
    except ImportError, e:
        continue

hasdoc = []
nodoc = []
for module in pymodules:
    if pymodules[module]:
        hasdoc.append(module)
    else:
        nodoc.append(module)

print 'module has no doc:'
for key in nodoc:
    print key + '|'

print '*' * 50

print 'module has doc:'
for key in hasdoc:
    print '[', key, ']'
    print pymodules[key]
    print '-' * 30

