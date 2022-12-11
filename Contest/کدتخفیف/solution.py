n1, n2 = input().split()
c = []
h = ""

for i in n2:
    if i not in c:
        c.append(i)

c.sort()
for i in c:
    h += i
m = []

for i in range(int(n1)):
    a = str(input())
    s = ""
    l = []
    for j in a:
        if j not in l:
            l.append(j)
    l.sort()
    for j in l:
        s += j
    if s == h:
        m.append("Yes")
    else:
        m.append("No")

print("\n".join(m))
