number = input().split()
n = int(number[0])
k = int(number[1])

hasani = 1
d = True
r = 0

while d == True:
    hasani += k

    if hasani > n:
        hasani = hasani - n
    if hasani == 1:
        d = False

    r += 1

print(r)
