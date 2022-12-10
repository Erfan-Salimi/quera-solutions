m = []
n = int(input())

for i in range(1, n):
    if n / i == int(n / i) and i != n:
        m.append(i)

print(max(m))
