import math

r = 0
number = input()
number = number.split()
factorial = math.factorial(int(number[0]))

for i in str(factorial):
    if number[1] == i:
        r += 1

print(r)
