n = input()
N = input().split()

for i in N:
    if int(i) <= 3:
        print(int(i) * "*")
    else:
        print("*")
