p, d = input().split(' ')
p = int(p)
d = int(d)
x = d

while x % p > p / 2:
    x += d

print(x)
