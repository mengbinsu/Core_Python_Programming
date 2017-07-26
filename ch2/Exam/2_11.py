#!/usr/bin/env python
def sum_five():
    print sum(int(raw_input('enter a number:')) for i in range(5))

def avg_five():
    print float(sum(int(raw_input('enter a number:')) for i in range(5))) / 5

while True:
    InputStr = raw_input("Enter orders[sum:avg:x]")
    if (InputStr == 'sum'):
        sum_five()
    elif (InputStr == 'avg'):
        avg_five()
    elif (InputStr == 'x'):
        print 'Exit'
        break;
