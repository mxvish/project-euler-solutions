#solution 1
def calc(x, y, total):
    if y < 4000000:
        if y % 2 == 0:
            total += y 
        z = x + y
        calc(y, z, total)
    else:
        print(total)

calc(1, 2, 0)

#solution 2
prev, cur = 0, 1
total = 0
while cur < 4000000:
    prev, cur = cur, prev + cur
    if cur % 2 == 0:
        total += cur 
print(total)
