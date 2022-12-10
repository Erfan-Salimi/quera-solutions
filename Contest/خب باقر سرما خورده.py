a = input()
b = input()
c = input()
d = input()
e = input()
dd = []

def fin(x1,x2):
    if((x1 or x2) in a ):
        dd.append(1)
    if ((x1 or x2) in b):
        dd.append(2)
    if ((x1 or x2) in c):
        dd.append(3)
    if ((x1 or x2) in d):
        dd.append(4)
    if ((x1 or x2) in e):
        dd.append(5)

fin("MOLANA","HAFEZ")
dd.sort()

print(" ".join(str(x) for x in dd))
