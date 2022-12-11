n = input()

n = n.split()
ax = int(n[0])
ay = int(n[1])
bx = int(n[2])
by = int(n[3])

if ax == bx:
    print("Vertical")
elif ay == by:
    print("Horizontal")
else:
    print("Try again")
