nomre = int(input())
safar = int(input())

if safar <= 0:
    print(20)
elif safar == 7:
    print(nomre)
else:
    if nomre - safar < 0:
        print(0)
    else:
        print(nomre - safar)
