n1 = input().split()
n2 = input().split()
n = int(n1[0])

s = 0
for i in range(n):
    if i <= 6:
        c = 31
    elif i < 12:
        c = 30
    else:
        c = 29
    s += c

N1 = s + int(n1[1])

h = 0
N = int(n2[0])

for i in range(N):
    if i <= 6:
        c = 31
    elif i < 12:
        c = 30
    else:
        c = 29
    h += c

N2 = h + int(n2[1])

if N1 < N2:
    print(N2-N1)
elif N2 < N1:
    print(N1-N2)
else:
    print(0)
