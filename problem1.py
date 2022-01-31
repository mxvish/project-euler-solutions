def calc(num):
    sum = 0
    for x in range(1,num):
        if x % 3 == 0 or x % 5 == 0:
           sum += x
    print(sum)

calc(10)
calc(1000)
