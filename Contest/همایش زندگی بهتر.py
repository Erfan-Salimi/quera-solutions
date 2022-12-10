n = input().split()

if int(n[1]) <= 10:
    jahat = "Right"
elif int(n[1]) >= 10:
    jahat = "Left"

radif = 11 - int(n[0])

if jahat == "Right":
    shomare = int(n[1])
elif jahat == "Left":
    shomare = 21 - int(n[1])

print(f"{jahat} {radif} {shomare}")
