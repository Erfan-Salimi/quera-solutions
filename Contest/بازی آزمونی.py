a, b, c, d = [int(i) for i in input().split()]

if d >= b:
    print("exam finished!")
elif d < a:
    print("exam did not started!")
else:
    if c + d > b:
        print(b - d)
    else:
        print(c)
