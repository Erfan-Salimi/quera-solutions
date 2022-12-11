n = int(input())
m = []

for i in range(1, n+1):
    if i == 1 or i == 2:
        m.append(i)
    else:
        m.append(m[i-2] + m[i-3])

for i in range(1, n+1):
    if i in m:
        d = True
    else:
        d = False

    if d == False:
        print(end="-")
    else:
        print(end="+")
    