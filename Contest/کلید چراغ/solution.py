r = 0
m = []
n = int(input())

for i in range(n):
    m.append(int(input()))

for i in range(len(m) - 1):
    if m[i] != m[i+1]:
        r += 1

print(r)
