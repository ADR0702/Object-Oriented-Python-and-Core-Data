
cuv1="roma"
cuv2="maro"

if len(cuv1) == len(cuv2):
    # dictionar cu cheie litere si valoare numar de iteratii
    dict_cuv1={}
    for ch in cuv1:
        dict_cuv1[ch]= dict_cuv1.get(ch,0)+1

    dict_cuv2={}
    for ch in cuv2:
        dict_cuv2[ch]= dict_cuv2.get(ch,0)+1

    if dict_cuv1==dict_cuv2:
        print("sunt anagrame")
    else:
        print("nu sunt anagrame")

    # sortarea lor intr-o lista

