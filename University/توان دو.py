n = int(input())

b = 0
i = 1

while b < n:
    b = 2 ** i
    i += 1

print(b)
