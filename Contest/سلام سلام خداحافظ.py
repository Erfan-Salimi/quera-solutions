n = int(input())
names = [i for i in input().split()]

for i in range(0, n):
    for j in range(i, 0, -1):
        print(names[i] + ": salam "+ names[j-1] + "!")

for i in range(0, n):
    print(names[i] + ": khodafez bacheha!")
    for j in range(i, n):
        if names[j] != names[i]:
            print(names[j] + ": khodafez "+ names[i] + "!")
