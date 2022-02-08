import math

a, b = 0, 0
key = 100
#key = 10

for x in range(key):
    a += math.pow(x+1, 2)
    b += x+1
print(a)
print(math.pow(b, 2))
print(abs(a-math.pow(b, 2)))
