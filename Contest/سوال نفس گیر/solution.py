n = int(input())
a = input().split()
b = input().split()
c = 0
m = 0

for i in range(n):
    c = int(a[i]) * int(b[i])
    m += c

print(m)
