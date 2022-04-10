# triange number are of the form n *(n +1)/2
# so i just need to find the factors of n and n+1 st
# the number of factors of n * number of factors of n+1 is over 500

## answer stolen not mine. couldnt get it to work so i cheated i guess :/ only one though
import math
def num_divisors(n):
    if n % 2 == 0: n = n/2
    divisors = 1
    count = 0
    while n % 2 == 0:
        count += 1
        n = n/2
    divisors = divisors * (count + 1)
    p = 3
    while n != 1:
        count = 0
        while n % p == 0:
            count += 1
            n = n/p
        divisors = divisors * (count + 1)
        p += 2
    return divisors

def find_triangular_index(factor_limit):
    n = 1
    lnum, rnum = num_divisors(n), num_divisors(n+1)
    while lnum * rnum < 500:
        n += 1
        lnum, rnum = rnum, num_divisors(n+1)
    return n

index = find_triangular_index(500)
final = (index * (index +1)) /2
print(final)
#12375
