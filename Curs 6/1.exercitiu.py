# V2
vocale= "aeiouAEIOU"
input_string="Salutare, ce mai faci?"
rezultat=""
for i in input_string:
    if i not in vocale:
        rezultat+=i
print(rezultat)

# V2
for i in input_string:
    if i not in vocale:
        print(i, end="")