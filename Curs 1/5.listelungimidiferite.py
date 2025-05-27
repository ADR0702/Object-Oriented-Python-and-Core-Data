lista_a=[1,2,3, 100, 200]
lista_b=[4,5,6]
lista_c=[]

if len(lista_a) > len(lista_b):
    min_lungimilor=len(lista_b)
    lista_lunga=lista_a
else:
    min_lungimilor=len(lista_a)
    lista_lunga=lista_b

    
for i in range(len(lista_b)):
    lista_c.append(lista_a[i]+lista_b[i])
print(lista_c)

lista_c+=lista_a[len(lista_b):]

print(lista_c)

