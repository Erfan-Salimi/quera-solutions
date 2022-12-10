n = input("").split()
s = 0

for i in n:
    i = int(i)
    if i >= 80:
         s += 1

if s > 2 :
    print("Mamma mia!")
elif s == 1 or s == 2:
    print("Mamma mia!!")
else:
    print("Mamma mia!!!")
