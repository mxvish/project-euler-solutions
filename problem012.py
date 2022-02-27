#time 3.00s user 0.03s system 98% cpu 3.076 total
import math

def calc(divisorCount):
    num, add = 0, 1
    divisors = []
    while len(divisors) < divisorCount:
        divisors = []
        num += add
        for x in range(1, int(math.sqrt(num))):
            if num%x == 0:
                divisors.append(x)
                divisors.append(num/x)
        add += 1
    print(num)
calc(500)
#calc(5)
