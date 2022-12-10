n, m = input().split()
n, m = int(n), int(m)

for i in range(n):
    print(m*"X"+m*"."+m*"X")

for i in range(n):
    print(m*"."+m*"X"+m*".")

for i in range(n):
    print(m*"X"+m*"."+m*"X")
