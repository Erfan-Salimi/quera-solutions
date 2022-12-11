a = input().split()
b = a[1]
l = a[2]
a = a[0]

if int(l) % 2 != 0:
    h = (int(l) - 1) / 2 #5 == 2
    j = int(l) - h #5 == 3

    k = int(a) * j
    p = int(b) * h

    sumsum = k + p
    print(int(sumsum))
    
elif int(l) % 2 == 0:
    h = int(l) / 2
    j = int(l) - h

    k = int(a) * j
    p = int(b) * h

    sumsum = k + p
    print(int(sumsum))
    