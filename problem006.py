#0.03s user 0.02s system 55% cpu 0.093 total
a, b = 0, 0
key = 100
#key = 10

for x in range(key):
    a += (x+1)*(x+1)
    b += x+1
print(a)
print(b*b)
print(abs(a-b*b))
