n = int(input())
r = []

for i in range(n):
    x, y = [int(j) for j in input().split()]
    
    if max(x, y) - min(x, y) in (0, 2):
        if x % 2 == 0:
            r.append(str(x+y))
        else:
            r.append(str(x+y-1))
    else:
        r.append(str(-1))

print("\n".join(r))
