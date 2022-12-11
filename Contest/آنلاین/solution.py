n = int(input())
result = 13
if n < 0:
    result += (1401 * -(n))
else:
    result -= (1401 * n)
print(result)
