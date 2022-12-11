n = input()
n = n.split()
a = int(n[0])
count = int(n[1])

for i in range(count):
    a /= 2

if a >= 0:
    print(int(a))
else:
    if int(a) != a:
        print(int(a) - 1)
    else:
        print(int(a))
