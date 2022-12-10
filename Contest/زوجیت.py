n = int(input())
s = 0

for i in range(1, n+1):
    if n % i == 0:
        s += 1

if n == 2:
    print("fard")
else:
    if n == 0:
        print("fard")
    if s == 2 and n % 2 != 0:
        print("zoj")
    else:
        print("fard")
