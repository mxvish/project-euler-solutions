"""
#solution 1
prime_numbers = [2]
num = 600851475143

for x in range(3, num + 1):
    for y in range(len(prime_numbers)):
        if x % prime_numbers[y] == 0 or num % x != 0:
            break
        if x not in prime_numbers and y == len(prime_numbers)-1:
            prime_numbers.append(x)

print(prime_numbers[len(prime_numbers) - 1])
"""

#solution 2 (less big-O complexity)
n = 600851475143
div, maxFact = 2, 0

while n != 0:
    if n % div != 0:
        div += 1
    else:
        maxFact = n
        n = n / div
        if n == 1:
            print(int(maxFact))
            break
