n = int(input())
N = input().split()

for i in range(len(N)):
    N[i] = int(N[i])

g = []
g = N.copy()
i = 0
m = []

N.sort()
g.sort()
g.reverse()

while True:
    if len(m)-1 >= len(N)-1:
        break
    
    m.append(str(g[i]))
    if len(m)-1 >= len(N)-1:
        break

    m.append(str(N[i]))
    i += 1

print(" ".join(m))
