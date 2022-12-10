from collections import Counter

m = []
n = input().split()
s = 0

for i in range(int(n[0])+int(n[1])):
    a = input().split()
    for j in range(int(a[0]), int(a[1])+1):
        m.append(j)

b = Counter(m)
for i in b:
    if b[i] > 1:
        s += 1

print(s)
