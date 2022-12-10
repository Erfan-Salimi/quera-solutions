number = input()
number = number.split()

n = float(number[0])
k = float(number[1])
s = float(number[2])

if s >= k * n:
    print("Kafie!")
else:
    print("Na! yeki bayad bere sabzi bekhare")
