n1 = int(input())
n2 = int(input())

for i in range(n1,n2 + 1):
    r = 0

    for j in range(1, i + 1):
        if i % j == 0:
            r += 1

    if r == 2:
        print(j)
