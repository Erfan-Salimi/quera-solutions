h = input().split()
N = int(h[0])
M = int(h[1])
n = []
m = []
v = 0

for i in range(N):
    n.append(input().split())

for i in range(M):
    m.append(input().split())

for i in m:
    
    c = n[int(i[0])-1]

    v += int(c[int(i[1])-1])

print(v)
