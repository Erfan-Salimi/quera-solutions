n1 = input().lower().split()
n2 = input().lower().split()

if n1[0] == n2[1] or n1[1] == n2[0] or n1[0] == n1[1] or n2[0] == n2[1]:
    print('YES')
else:
    print('NO')
