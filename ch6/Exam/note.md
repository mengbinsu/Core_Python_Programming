##练习
####6.1字符串.string 模块中是否有一种字符串方法或者函数可以帮我鉴定一下一个字符串是否是另一个大字符串的一部分?

```
string.find(), string.index()
```

####6.2字符串标识符.修改例 6-1 的 idcheck.py 脚本,使之可以检测长度为一的标识符,并且可以识别 Python 关键字,对后一个要求,你可以使用 keyword 模块(特别是 keyword.kelist)来帮你.

```
#!/usr/bin/env python

import string
import keyword

alphas = string.letters + '_'
nums = string.digits

print 'Welcome to the Identifier Checker v1.0'
print 'Testees must be at least 2 chars long.'
myInput = raw_input('Identifier to test? ')

if myInput[0] not in alphas:
    print 'invalid: first symbol must be alphabetic'
else:
    if len(myInput) == 0:
        print 'okay as an identifier'
    else:
        for otherChar in myInput[1:]:
            if otherChar not in alphas + nums:
                print 'invalid:remaining symbols must be alphabetic '
                break;
        if keyword.iskeyword(myInput):
            print 'invalid:input string is a keyword'
        else:
            print 'okay as an identifier'
```

####6.3. 排序 (a) 输入一串数字,从大到小排列之. (b) 跟a一样,不过要用字典序从大到小排列之.

```
#!/usr/bin/env python
import string

def des_sort_numstr_by_decimal(numstr):
    numlist = numstr.split(',')
    for i in range(0, len(numlist)):
        numlist[i] = int(numlist[i])

    numlist.sort()
    numlist.reverse()
    return numlist

def des_sort_numstr_by_dictionary(numstr):
    numlist = numstr.split(',')
    numlist.sort()
    numlist.reverse()
    return numlist

if __name__ == '__main__':
    numstr = raw_input('input some numbers: ')
    print 'before sort: ' + numstr
    print 'sort by decimal:' + str(des_sort_numstr_by_decimal(numstr))
    print 'sort by dictionary:' + str(des_sort_numstr_by_dictionary(numstr))
```


