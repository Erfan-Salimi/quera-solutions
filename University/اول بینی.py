n1 = int(input())
n2 = int(input())
s = []

for i in range(n1+1, n2):
    r = 0
    for j in range(2, i):
        if i % j == 0:
            r += 1
    if r == 0:
        s.append(str(i))

print(",".join(s))
