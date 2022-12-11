n = int(input())
s = 0

for i in range(n):
    m = []

    for j in range(2):
        n = input()
        b = len(n.replace(" ", ""))
        m.append(b)
    s += m[0] - m[1]

print(s)
