
import sys
test_cases = open('cases.txt', 'r')
for test in test_cases:
    if test == None: break
    print test.lower()


test_cases.close()