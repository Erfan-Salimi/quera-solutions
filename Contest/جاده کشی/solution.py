n = int(input())

if n % 2  == 0 :
    a = n / 2
    b = a
else:
    n += 1
    a = n / 2
    b = (n / 2) - 1

print(int((a + 1) * (b + 1)))