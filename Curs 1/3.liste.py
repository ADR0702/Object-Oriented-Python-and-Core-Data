a=[1,2,3]
b=[4,5,6]
c=[]

# iteratie
# for i in a:
#     print("i=", i)
c=[]
for i in range(len(a)):
    print("i=", i)
    c.append (a[i]+b[i])

print(c)