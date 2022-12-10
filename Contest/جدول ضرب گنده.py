n = int(input())
number = []

for i in range(1, n + 1):
    number.append(i)

for j in range(1, n+1):
    for t in number:
        print(end=f'{t * j} ')
    print("")
