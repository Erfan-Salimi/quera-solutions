n = input().split()
d = [1, 1, 2, 2, 2, 8]

for i in range(len(n)):
    print(end=f"{d[i] - int(n[i])} ")
