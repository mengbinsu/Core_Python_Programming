#/usr/bin/env python

import re, os

def checkurl(url):
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    if regex.match(url):
        return True
    else:
        return False

def geturl():
    name = raw_input('Please input a url name: ')
    while 1:
        url = raw_input('Please input a url address: ')
        if checkurl(url):
            break;
        else:
            print 'wrong url format, please input again'

    mark = raw_input('Please input a url mark: ')
    folder = raw_input('Please input a url folder: ')
    return (name, url, mark, folder)

def load(filename):
    f = open(filename, 'a+')
    bmlist = f.readlines()
    f.close()
    return bmlist

def save(bmlist, filename):
    f = open(filename, 'w+')
    for line in bmlist:
        if len(line) == 0:
            continue
        f.write(line)
    f.close()

def add(bmlist, name, url, mark, folder='default'):
    bookmark = name + ';' + url + ';' + mark + ';' + folder + os.linesep
    if bookmark not in bmlist:
        bmlist.append(bookmark)

def modify(bmlist, index, name, url, mark, folder):
    bmlist[index] = name + ';' + url + ';' + mark + ';' + folder + os.linesep

def delbm(bmlist, index):
    bmlist.pop(index)

def findbk(bmlist, fname, furl):
    for i, item in enumerate(bmlist):
        (name, url, mark, folder) = item.split(';')
        if fname and furl:
            if (fname in name) and (furl in url):
                return i

        if fname and (fname in name):
            return i

        if furl and (furl in url):
            return i
    else:
        return -1

def output2html(bmlist):
    for i, item in enumerate(bmlist):
        (name, url, mark, folder) = item.split(';')
        os.mkdir(folder.strip())
        filename = name.strip() + '.html'
        f = open(filename, 'w+')
        fmt = '%d\t%s\t<a href=%s>%s</a>\t%s<br>'
