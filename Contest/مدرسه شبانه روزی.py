def gcd(x, y):
    if (x < y):
        temp = x
        x = y
        y = temp

    while (y != 0):
        remainder = x % y
        x = y
        y = remainder

    r = x
    return r


n = int(input())
m = []

for i in range(n):
    m.append(int(input()))
s = m[0]

for i in range(1, len(m)):
    s = int((m[i] * s) / gcd(m[i], s))

print((s%30)+1)
