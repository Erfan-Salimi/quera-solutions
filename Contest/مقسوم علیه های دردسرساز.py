n = int(input())
d = 0
b = 0

for i in range(1, n+1):
    for j in range(1, int(i/2)+1):
        if i % j == 0:
            b += 1
            d += j
    b += 1
    d += i

print(b, d)
