m = []
n = int(input())
d = True
s = 0

for i in range(n):
    m.append(int(input()))

c = sum(m) / n
for i in m:
    if i <= c:
        s += c - i

print(int(s))
