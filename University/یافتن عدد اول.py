n = input()
m = []
for i in n:
    m.append(int(i))

c = sum(m)
i = int(n)+1
h = 0

while True:
    s = 0
    for j in range(1, i):
        if i % j == 0:
            s += 1
    if s == 1:
        h += 1
        if h == c:
            print(i)
            break
    i += 1
