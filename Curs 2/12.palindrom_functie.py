

def este_palindrom(cuvant):
    return cuvant== cuvant[:-1]
print(este_palindrom("caicac"))
print(este_palindrom("maro"))



def este_palindromv2(cuvant):
    return list(cuvant) == list(reversed(cuvant))


print(este_palindromv2("caiac"))
print(este_palindromv2("maro"))