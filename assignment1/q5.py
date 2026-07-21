def x(a,b,c):
    if a>b and a>c:
        return a
    elif b>c:
        return b
    else:
        return c
a=(int(input("enter 1st number")))
b=(int(input("enter 2nd number")))
c=(int(input("enter 3rd number")))
print("greatest num is",x(a,b,c))
