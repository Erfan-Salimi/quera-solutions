from math import *

n = int(input())
m = []

for i in range(n):
    a = input().split()
    l = int(a[0])
    r = int(a[1])

    if int(sqrt(l)) == sqrt(l):
        m.append(str(int(sqrt(r)) - int(sqrt(l)) + 1))
    else:
        m.append(str(int(sqrt(r)) - int(sqrt(l))))

print("\n".join(m))
