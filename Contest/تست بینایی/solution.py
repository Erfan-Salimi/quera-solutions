n = int(input())
a = input()
b = input()

w = 0
for i in range(n):
    if a[i] != b[i]:
        w += 1

print(w)