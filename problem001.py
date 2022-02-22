#0.04s user 0.02s system 68% cpu 0.088 total
def calc(num):
    sum = 0
    for x in range(1,num):
        if x % 3 == 0 or x % 5 == 0:
           sum += x
    print(sum)

calc(10)
calc(1000)
