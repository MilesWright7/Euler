i = 1
sum1 = 0
sum2 = 0
while i < 101:
    sum1 += i
    sum2 = i*i + sum2
    i += 1
sum1 = sum1 * sum1
final = sum1 - sum2
print(final)
