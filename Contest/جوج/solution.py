n = int(input())
b = input().split()

s = False
for i in range(n):
    if i != 0 and i != n-1:
        if int(b[i]) > int(b[i-1]) and int(b[i]) > int(b[i+1]):
            s = True

if s == True:
    print("Ey baba :(")
else:
    print("Bah Bah! Ajab jooji!")
