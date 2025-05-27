def fun(x,y,z):
    return x+y**2+z//2

print(fun(z=2, x=3, y=6))

def fun(**a):
    return (min(a)+ min(a))/2
print(fun(11,29,51,-31,20))