dictionar={"cal":"alb", "pepene":"rosu", "dode":"negru"}
# iterare
for i in dictionar:
    print([i], dictionar[i])
# iterare prin chei valoare
for i in dictionar.items():
    print(i)

for k, v in dictionar.items():
    print(k, v)
# citire
print(dictionar["cal"])
# inserare
dictionar["mugurel"]="verde"
print(dictionar)

dictionar["dodge"]="albastru"
print(dictionar)


# nerecomandat de a avea key numere
dictionar[5]="cinci"
print(dictionar)

dictionar[()]="Hello"
print(dictionar)