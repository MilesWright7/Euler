primes = [2, 3, 5, 7, 11]
i = 13
isprime = True
while len(primes) < 10001:
    for item in primes:
        if i % item == 0:
            isprime = False
            break
    if isprime:
        primes.append(i)
    i += 1
    isprime = True

print(primes[-1])
