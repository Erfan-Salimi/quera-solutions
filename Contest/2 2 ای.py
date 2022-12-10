n = int(input())
n = str(bin(n))[0] + str(bin(n))[2:]
a = "10101111001"

if int(n, 2) <= int(a, 2):
    print("NO")
else:
    print("YES")
