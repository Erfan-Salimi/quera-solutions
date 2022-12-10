n = int(input())
a = input()
a1, a2 = (a[:int(len(a)/2)], a[int(len(a)/2):])

b = True
for i in range(n):
    if a1[i] == a2[i]:
        b = False

if b:
    print("YES")
else:
    print("NO")
