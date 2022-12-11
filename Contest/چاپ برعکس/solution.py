n = input()
numbers = []
b = 0

while n != "0":
    numbers.append(n)
    n = input()
    b += 1

numbers = numbers[::-1]

for i in numbers:
    print(i)
