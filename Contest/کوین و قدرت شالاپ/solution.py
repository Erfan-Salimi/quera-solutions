n = int(input())

if n % 2 == 0:
    s = n**2 / ((n +1)*4)
else:
    s = (n-1) / 4

print(s)
