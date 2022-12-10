n = input()
N = []

for i in n:
    N.append(i)

for i in range(len(N)):
    for j in range(i):
        N[j] = N[i]
    print("".join(N))
