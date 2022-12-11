k = int(input())
ramz = input()
m = []
s = 0

for i in range(k):
    a = input()
    ind = a.index(ramz[i])
    if ind > 4:
        s += 9 - ind 
    else:
        s += ind

print(s)
