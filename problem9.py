#solution 1
"""
import math, sys

total = 1000
#total = 12

for a in range(1, int(total/3)):
    for b in range(a+1, int(total/2)):
        for c in range(b+1, total):
            if a+b+c == total and math.pow(a,2) + math.pow(b,2) == math.pow(c,2):
                print(a, b, c, a*b*c)
                sys.exit()
"""
#solution 2(less time complexity, 0.05s user 0.02s system 80% cpu 0.085 total)
import sys

total = 1000
#total = 12

for a in range(1, int(total/3)):
    for b in range(a+1, int(total/2)):
        c = total - a - b
        if a*a + b*b == c*c:
            print(a, b, c, a*b*c)
            sys.exit()
