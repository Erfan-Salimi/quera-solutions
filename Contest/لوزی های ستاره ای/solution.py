n = int(input())

if n == 1:
    print("*")
else:
    for i in range(1, n+1, 2):
        space = int((n - i) / 2)
        print(space * " " + i * "*" + space * " " + space * " " + i * "*" + space * " ")

    for i in range(n-2, 0, -2):
        space = int((n - i) / 2)
        print(space * " " + i * "*" + space * " " + space * " " + i * "*" + space * " ")
