XY = input().split()
x = int(XY[0])
y = int(XY[1])

zel = int(input())

XY2 = input().split()
x2 = int(XY2[0])
y2 = int(XY2[1])

if x2 <= (x + zel) and x2 >= x and y2 >= (y-zel) and y2 <= y :
    xy = True
else:
    xy = False

if xy == True:
    print("Mahdi")
else:
    print("Parsa")
