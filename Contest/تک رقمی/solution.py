n = int(input())

while n >= 10:
    b = 0
    for i in str(n):
        b += int(i)
    n = b

print(n)
