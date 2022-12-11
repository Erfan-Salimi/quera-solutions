n = int(input())
n1 = input().split()
n2 = input().split()
m = []

for j in range(n):
    n1[j] = int(n1[j])

for i in range(n):
    n2[i] = int(n2[i])
    if n2[i] == 1:
        m.append(n1[i])

m.sort()
for t in m:
    print(end=f"{t} ")
