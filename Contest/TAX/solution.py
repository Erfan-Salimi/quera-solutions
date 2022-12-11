m = []

while True:
    n = int(input())
    if n == 0:
        break
    else:
        m.append(n)

for i in m:
    if i <= 1000000:
        print(i)
    elif i > 1000000 and i <= 5000000:
        c = int(i / 100)
        b = c * 10
        print(i-b)
    else:
        c = i / 100
        b = c * 20
        if c != int(c):
            print(i-b)
        else:
            print(int(i-b))
