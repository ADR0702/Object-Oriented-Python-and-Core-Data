
def este_palindrom(cuv):
    for i in range(len(cuv)):
        if cuv[i]!=cuv[-1-i]:
            print("cuvantul nu este palindrom")
            break
    else:
        print("cuvantul este palindrom")



cuvant ="caiac"
este_palindrom(cuvant)

