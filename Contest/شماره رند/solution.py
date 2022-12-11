from collections import Counter

n = int(input())
m = []
u = []

for i in range(n):
    h = []
    t = input()

    for i in t:
        h.append(i)

    d = False
    b = Counter(h)

    for j in b:
        if b[j] >= 4:
            d = True

    if t[::-1] == t:
        d = True

    for j in range(len(h)-2):
        if int(h[j]) == int(h[j+1]) == int(h[j+2]):
            d = True

    if len(h) < 8:
        d = False

    if d == True:
        u.append("Ronde!")
    else:
        u.append("Rond Nist")

for i in u:
    print(i)
