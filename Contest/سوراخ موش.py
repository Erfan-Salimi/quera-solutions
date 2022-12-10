n = input()
n = n.split()
n1 = int(n[0])
n2 = int(n[1])

if n2 > n1:
    s = n2 - n1
    for i in range(s):
        print(end="R")

elif n2 < n1:
    s = n1 - n2
    for i in range(s):
        print(end="L")

else:
    print("Saal Noo Mobarak!")
