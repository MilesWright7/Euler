a = 1
b = 1
c = 1
d = 0
for i in range(1,1000):
    a = i * i
    for j in range(1,1000):
        b = j*j
        for x in range(1,1000):
            c = x * x
            d = i + j + x
            if d == 1000:
                left = a + b
                if left == c:
                    print(i*j*x)
