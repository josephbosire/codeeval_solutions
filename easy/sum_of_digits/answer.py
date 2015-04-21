
import sys
test_cases = open('cases.txt', 'r')
for test in test_cases:
    if test == None: break
    sum = 0;
    for num in range(0, len(test)-1):
        sum += int(test[num])
    print sum


test_cases.close()