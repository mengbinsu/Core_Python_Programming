##练习

####5.1整形。讲讲Python普通整形和长整形的区别。

**普通整形：**和机器位数有关，32位：最大值2的31次方-1，64位：2的63方-1

**长整形：**表示的最大值只与机器的内存有关，普通整形“溢出“时Python将其自动转换为长整形。

####5.2运算符。 (a) 写一个函数，计算并返回两个数的乘积 (b) 写一段代码调用这个函数，并显示它的结果

```
#!/usr/bin/env python
def ultiplay(num1, num2):
	return num1 * num2
print multiplay(10, 10)
```
####5.3 标准类型运算符. 写一段脚本，输入一个测验成绩，根据下面的标准，输出他的评分成绩（A-F）。 A: 90–100 B: 80–89 C: 70–79 D: 60–69 F: < 60

```
#!/usr/bin/env python
def is_leap_year(year):
    if year % 4  == 0:
            if year % 100 != 0:
                return True
            elif year % 400 == 0:
                return True
            else:
                return False
    else:
        return False

print is_leap_year(2000)
print is_leap_year(2004)
print is_leap_year(2100)
```
####5.5取余。取一个任意小于1美元的金额，然后计算可以换成最少多少枚硬币。硬币有1美分，5美分，10美分，25美分四种。1美元等于 100 美分。举例来说，0.76 美元换算结果 应该是3枚25美分， 1 枚1美分。类似76枚1美分，2枚25 美分+2枚10美分+1枚5美分+1枚 1 美分这样的结果都是不符合要求的。

```
#!/usr/bin/env python
def get_cent_count(num):
    cent_count_arr = []
    cents = [25, 10, 5, 1]

    left = num
    i = 0
    while left != 0:
        cent_count_arr.append(left // cents[i])
        left %= cents[i]
        i += 1

    return cent_count_arr
```

####5.6 算术。写一个计算器程序 你的代码可以接受这样的表达式，两个操作数加一个运算符： N1 运算符 N2. 其中 N1 和 N2 为整数或浮点数，运算符可以是+, -, *, /, %, ** 分别表示 加法，减法， 乘法， 整数除，取余和幂运算。计算这个表达式的结果，然后显示出来。提示： 可以使用字符串方法 split(),但不可以使用内建函数 eval().

```
#!/usr/bin/env python
import decimal

def num1_op_num2(op_str):
    arr = op_str.split()
    op = arr[1]
    num1 = decimal.Decimal(arr[0])
    num2 = decimal.Decimal(arr[2])

    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        return num1 / num2
    elif op == '%':
        return num1 % num2
    elif op == '**':
        return num1 ** num2
    else:
        raise ValueError("op don't exist ")
```

####5.10 转换。写一对函数来进行华氏度到摄氏度的转换。转换公式为 C = (F - 32) * (5 / 9) 应该在这个练习中使用真正的除法， 否则你会得到不正确的结果。
```
#!/usr/bin/env python

from __future__ import division

def tran_F_to_C(F):
    C = (F - 32) * (5 / 9)
    return round(C, 2)
```

####5.15最大公约数和最小公倍数。请计算两个整数的最大公约数和最小公倍数。

[最大公约数和最小公倍数算法](https://www.idomaths.com/zh-Hans/hcflcm.php)

```
#!/usr/bin/env python

def gcd(num1, num2):
    while num2 > 0:
        tmp = num1 % num2
        num1 = num2
        num2 = tmp
    return num1

def lcm(num1, num2):
    return num1 * num2 / gcd(num1, num2)
```

####5.16 家庭财务。给定一个初始金额和月开销数， 使用循环，确定剩下的金额和当月的支出数， 包括最后的支出数。 Payment() 函数会用到初始金额和月额度， 输出结果应该类似下 面的格式（例子中的数字仅用于演示）：

```
#!/usr/bin/env python

def pay():
    balance = float(raw_input('Enter opening balance: '))
    balance = round(balance, 2)
    payment = float(raw_input('Enter monthly payment: '))
    payment = round(payment, 2)

    print '\tAmount\tRemainning'
    print 'Pymt#\tPaid\tBalance'
    print '-----\t----\t---'

    print '0\t$0.00\t$%s' %balance
    i = 1
    while balance > payment:
        balance -= payment
        balance = round(balance, 2)
        i += 1
        print '%d\t$%s\t$%s' %(i, payment, balance)
    print '%d\t$%s\t$0.00' %(i, balance)
```

####5.17 随机数。熟读随机数模块然后解下面的题： 生成一个有 N 个元素的由随机数 n 组成的列表， 其中 N 和 n 的取值范围分别为： (1 < N <= 100), (0 <= n <= 2^31 -1)。然后再随机从这个列表中取 N (1 <= N <= 100)个随机数 出来， 对它们排序，然后显示这个子集。
```
#!/usr/bin/env python

def pay():
    balance = float(raw_input('Enter opening balance: '))
    balance = round(balance, 2)
    payment = float(raw_input('Enter monthly payment: '))
    payment = round(payment, 2)

    print '\tAmount\tRemainning'
    print 'Pymt#\tPaid\tBalance'
    print '-----\t----\t---'

    print '0\t$0.00\t$%s' %balance
    i = 1
    while balance > payment:
        balance -= payment
        balance = round(balance, 2)
        i += 1
        print '%d\t$%s\t$%s' %(i, payment, balance)
    print '%d\t$%s\t$0.00' %(i, balance)
```










