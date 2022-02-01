prime_numbers = [2]
num = 600851475143

for x in range(3, num + 1):
    for y in range(len(prime_numbers)):
        if x % prime_numbers[y] == 0 or num % x != 0:
            break
        if x not in prime_numbers and y == len(prime_numbers)-1:
            prime_numbers.append(x)

print(prime_numbers[len(prime_numbers) - 1])
