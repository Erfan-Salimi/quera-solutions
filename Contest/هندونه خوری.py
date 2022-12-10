n = int(input())
m = input().split()

for i in range(len(m)):
    m[i] = int(m[i])

MAX = max(m)
r = 0

for i in m:
    if m[r] == MAX:
        print(r+1)
    r += 1
