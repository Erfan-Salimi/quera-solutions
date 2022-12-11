n = int(input())
m = []
toolha = []

for i in range(n):
    harf = []
    for i in input():
        harf.append(i)
    m.append(harf)

b = 0
for j in m:
    m[b] = set(j)
    b += 1

for t in m:
    toolha.append(len(t))

print(max(toolha))
