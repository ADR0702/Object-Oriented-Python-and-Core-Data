dictionar={"cal":"alb", "pepene":"rosu", "dode":"negru"}



if "piersica" in dictionar:
    print(dictionar["piersica"])
else:
    print("piersica nu exista")

print(dictionar.get("piersica"))

print(dictionar.get("cal"))
print(dictionar.get("piersica", "nereusit"))