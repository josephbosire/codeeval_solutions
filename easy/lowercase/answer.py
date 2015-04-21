
import sys
test_cases = open('cases.txt', 'r')
for test in test_cases:
    if test == None: break
    x,n = test.split(",")
    x = int(x)
    n = int(n)
    if n > x :
        print n
    else:
        for i in range(2,x):
            if(n*i) > x:
                print n *i
                break

test_cases.close()