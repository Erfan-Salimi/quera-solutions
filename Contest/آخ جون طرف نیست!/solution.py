def my_function(x):
  return list(dict.fromkeys(x))

rooz2 = []
r = 0
n1 = int(input())
n2 = input().split()

for i in n2:
    rooz2.append(i)

a1 = int(input())
a2 = input().split()

for i in a2:
    rooz2.append(i)

e1 = int(input())
e2 = input().split()

for i in e2:
    rooz2.append(i)

rooz = ["shanbe", "1shanbe", "2shanbe", "3shanbe", "4shanbe", "5shanbe", "jome"]
rooz2.sort()

rooz2 = my_function(rooz2)
for i in range(7):
    if rooz[i] not in rooz2:
        r += 1

print(r)
