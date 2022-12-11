n1 = input().split()
n2 = input().split()
n3 = input().split()
n4 = input().split()

for i in range(3):
    n1[i] = int(n1[i])
    n2[i] = int(n2[i])
    n3[i] = int(n3[i])
    n4[i] = int(n4[i])

man1 = max(n1)
man2 = max(n2)
man3 = max(n3)
man4 = max(n4)

MAX = max(int(man1), int(man2), int(man3), int(man4))

if MAX == man1:
    print("1")
elif MAX == man2:
    print("2")
elif MAX == man3:
    print("3")
else:
    print("4")
