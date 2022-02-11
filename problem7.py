#solution1
"""
prime_numbers = [2]
count, num = 2, 3 
key = 10001 
#key = 6

while count <= key:
    for x in range(len(prime_numbers)):
        if num % prime_numbers[x] == 0:
            break
        if x == len(prime_numbers) -1:
            prime_numbers.append(num)
            count += 1
    num += 2 
print(prime_numbers[len(prime_numbers)-1])
"""

#solution2 
#3.36s user 0.05s system 96% cpu 3.523 total
num = 10001
primes = [2]
attempt = 3
while len(primes) < num:
    if all(attempt % x != 0 for x in primes):
        primes.append(attempt)
    attempt += 2
print(primes[-1])
