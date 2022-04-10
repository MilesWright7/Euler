primes = [2,3,5,7,11]
i = 12
sum1 = 0
isprime = True
while i < 2000000:
    for prime in primes:
        if i % prime == 0:
            isprime = False
            break
    if isprime:
        primes.append(i)
    if i % 1000 == 0:
        print(i)
    i += 1
    isprime = True

for prime in primes:
    sum1 += prime
print(sum1)
