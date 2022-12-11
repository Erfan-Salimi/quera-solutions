from typing import Counter

n = int(input())

def feshorde(n):
    n = str(n)
    m = []

    for i in n:
        m.append(i)

    tekrar = ''
    b = Counter(m)

    for i in b:
        if b[i] > 1:
            tekrar += str(b[i])

    l = set(m)
    sorted(l)
    tekrar += ''.join(l)
    M = []

    for i in tekrar:
        M.append(i)

    M = sorted(M)
    return ''.join(M)


a = feshorde(n)

while True:
    b = feshorde(a)

    if b == a:
        break

    a = feshorde(b)

    if b == a:
        break

print(b)