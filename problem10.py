primes = [2]
maxnum = 2000000
#maxnum = 10
key = 1 

while key < maxnum-2:
    key += 2
    if all(key % x != 0 for x in primes):
        primes.append(key)

print(sum(primes))
