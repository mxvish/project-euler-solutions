maxNum, x, y = 0, 0, 0
#a, b = 100, 100
#digit, limit = 4, 9
a, b = 1000, 1000
digit, limit = 6, 99

default_b = b

while len(str(a*b)) >= digit and a > limit:
    a -= 1

    while b > limit:
        b -= 1
        num = a * b

        if num % 11 != 0:
            continue

        strNum = str(num)
        length = len(strNum)
        key = 0

        while (key + 1) * 2 <= length:
            if strNum[key] != strNum[length - key - 1]:
                break
            
            if (key + 1) * 2 == length and num > maxNum:
                maxNum, x, y = num, a, b

            key += 1

    b = default_b

print(x, y, maxNum)

