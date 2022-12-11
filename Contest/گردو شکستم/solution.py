n, x, y = map(int, input().split())

for i in range(0, n//x+1):
    if ((n - i * x) / y).is_integer():
        print(i, (n-i*x)//y)
        exit()

print(-1)
