ls = ["B", "KiB", "MiB"]

for i in range(int(input())):
    n = int(input())
    i = 0
    while n >= 1024:
        i += 1
        n = int(n/1024)
    print(f"{n}{ls[i]}")
