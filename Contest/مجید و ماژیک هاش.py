from collections import Counter

m = []
h = []
s = []
n = int(input())
N = input().split()

b = Counter(N)
for i in b:
    m.append(int(b[i]))

d = min(m)
for i in b:
    if b[i] == d:
        s.append(int(i))

print(min(s))
