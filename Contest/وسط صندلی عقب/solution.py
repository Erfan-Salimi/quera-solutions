m = []
s = []
n = []

for i in range(4):
    a = input().split()
    m.append(a[1])
    n.append(a[0])

for i in range(len(m)):
    if m[i] == 'R':
        s.append(n[i])
    elif m[i] == 'L':
        s.insert(0,n[i])

print(s[1])
