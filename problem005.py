#solution1
"""
def gcf(a, b):
    if b == 0:
        return a
    else:
        return gcf(b, a%b)

def lcm(a, b):
    d = gcf(a, b)
    return a/d*b

numbers = []
key = 20
#key = 10

for x in range(1, key+1):
    numbers.append(x)

while len(numbers) > 1:
    numbers.append(lcm(numbers[0], numbers[1]))
    del numbers[:2]
print(numbers)
"""

#solution2
#0.47s user 0.17s system 135% cpu 0.471 total
import numpy as np

numbers = []
key = 20
#key = 10

for x in range(1, key+1):
    numbers.append(x)

print(np.lcm.reduce(numbers))
