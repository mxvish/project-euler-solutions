#solution 1: takes longer than 1 min
"""
primes = [2]
maxnum = 2000000
#maxnum = 10
key = 1 

while key < maxnum-2:
    key += 2
    if all(key % x != 0 for x in primes):
        primes.append(key)

print(sum(primes))
"""

#solution 2: 2.61s user 0.03s system 99% cpu 2.653 total
def sum_primes(limit):
    primes = [2]
    for n in range(3, limit+1, 2):
        for p in primes:
            if n % p == 0: break   
            if n < p*p:
               primes.append(n)    
               break
        else: primes.append(n)     
    return sum(primes)
    
print(sum_primes(2000000))
