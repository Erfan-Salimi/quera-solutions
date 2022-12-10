n, mabna = input().split()
n, mabna = int(n), int(mabna)

a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
result = ''

while n:
    result += a[n % mabna]
    n //= mabna

result = result[::-1]
s1 = 0
s2 = 0

for i in range(0, len(result), 2):
    s1 += int(result[i])

for i in range(1, len(result), 2):
    s2 += int(result[i])

if s1 == s2:
    print('Yes')
else:
    print('No')
