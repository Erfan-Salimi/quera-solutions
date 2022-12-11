n1 = input()
n2 = int(n1[::-1])

a1 = input()
a2 = int(a1[::-1])

if n2 < a2:
    print(f"{n1} < {a1}")
elif n2 == a2:
    print(f"{n1} = {a1}")
else:
    print(f"{a1} < {n1}")
