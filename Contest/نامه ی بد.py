from collections import Counter

n = input()
b = Counter(n)
m = []
s = 0

for i in n:
    m.append(i)

m = set(m)
for i in b:
    if int(b[i]) % 2 == 0:
         s += 1

if s == len(m):
    print("khoob")
else:
    print("bad")
