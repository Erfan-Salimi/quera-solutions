from collections import Counter

a, b, c = input().split()
n1, N1 = input().split()
n2, N2 = input().split()
n3, N3 = input().split()

m = []
s = 0

for i in range(int(n1), int(N1)):
    m.append(i)
for i in range(int(n2), int(N2)):
    m.append(i)
for i in range(int(n3), int(N3)):
    m.append(i)

f = Counter(m)
for i in f:
    if f[i] == 1:
        s += int(a)
    elif f[i] == 2:
        s += int(b) + int(b)
    elif f[i] == 3:
        s += int(c) + int(c) + int(c)

print(s)
