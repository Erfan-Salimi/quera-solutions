m = []
p = 0

n = int(input())
n2 = input().split()

for o in n2:
    m.append(int(o))

for i in range(1, 1001):
    s = 0
    for j in m:
        if i % (j) == 0:
            s += 1
        if s == n:
            p += 1

print(p)
