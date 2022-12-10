keyvoon	= "331122"
nezam = "123"
shir_farhad	= "2123"

keyvoon_score = 0
nezam_score = 0
shir_farhad_score = 0

n = int(input())
s = input()

while True:
    if len(keyvoon) < n or len(nezam) < n or len(shir_farhad) < n:
        if len(keyvoon) < n:
            keyvoon += keyvoon
        if len(nezam) < n:
            nezam += nezam
        if len(shir_farhad) < n:
            shir_farhad += shir_farhad
    else:
        break

max_score = 0
max_score_names = []

for i in range(n):
    if s[i] == keyvoon[i]:
        keyvoon_score += 1
        if max_score < keyvoon_score:
            max_score = keyvoon_score
    
    if s[i] == nezam[i]:
        nezam_score += 1
        if max_score < nezam_score:
            max_score = nezam_score
    
    if s[i] == shir_farhad[i]:
        shir_farhad_score += 1
        if max_score < shir_farhad_score:
            max_score = shir_farhad_score

print(max_score)

if keyvoon_score == max_score:
    max_score_names.append("keyvoon")
if nezam_score == max_score:
    max_score_names.append("nezam")
if shir_farhad_score == max_score:
    max_score_names.append("shir farhad")

print("\n".join(max_score_names))
