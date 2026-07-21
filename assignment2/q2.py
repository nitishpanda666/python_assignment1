data=[10,12,15,18,20,20,22,25]
n=len(data)
if n%2==0:
    median=(data[n//2-1]+data[n//2])/2
else:
    median=data[n//2]
print("median=",median)