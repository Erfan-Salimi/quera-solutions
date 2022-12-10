n = input().split()
n1 = int(n[0])
n2 = int(n[1])
m = []

for i in range(n1):
    m.append(int(input()))

SUM = sum(m)

if SUM >= n2:
    print("YES")
else:
    print("NO")
