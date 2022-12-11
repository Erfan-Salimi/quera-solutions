N = int(input())
b = 0

for i in range(1, N):
    if N % i == 0:
        b += i

if b == N:
    print("YES")
else:
    print("NO")
