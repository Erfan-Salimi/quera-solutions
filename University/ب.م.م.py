n1 = int(input())
n2 = int(input())

def hcfnaive(n1, n2):
    a = n1
    b = n2

    if (b == 0):
        return a
    else:
        return hcfnaive(b, a % b)


print(hcfnaive(n1, n2))
