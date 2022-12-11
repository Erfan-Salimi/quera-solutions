a, b = int(input()), int(input())

if b >= a:
    print("Wrong order!")
elif (a - b) % 2 != 0:
    print("Wrong difference!")
else:
    for i in range(0, a):
        if i < (int((a-b)/2)) or i > a-(int((a-b)/2))-1:
            print("* " * a)
        else:
            print("* " * int((a-b)/2) + "  " * b + "* " * int((a-b)/2))
