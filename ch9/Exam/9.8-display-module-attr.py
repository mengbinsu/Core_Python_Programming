#!/usr/bin/env python
import importlib

def get_module_attr(module_name):
    module = importlib.import_module(module_name)
    attrs = dir(module)
    res = []

    for attr in attrs:
        value = getattr(module, attr)
        res.append({'name':attr, 'type':type(value), 'value':value})
    return res

for attr in get_module_attr('math'):
    print 'name:%s\t type:%s\t value:%20s' %(attr['name'], attr['type'],attr['value'])
