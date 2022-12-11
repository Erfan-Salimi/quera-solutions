n1 = input().split()
n1x = int(n1[0])
n1y = int(n1[1])

n2 = input().split()
n2x = int(n2[0])
n2y = int(n2[1])

n3 = input().split()
n3x = int(n3[0])
n3y = int(n3[1])

if n1x == n2x:
    n4x = n3x
if n1x == n3x:
    n4x = n2x
if n2x == n3x:
    n4x = n1x
if n1y == n2y:
    n4y = n3y
if n1y == n3y:
    n4y = n2y
if n2y == n3y:
    n4y = n1y

print(f"{n4x} {n4y}")
