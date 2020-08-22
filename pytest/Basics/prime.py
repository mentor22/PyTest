import math
x=int(input("input a positive number : "))
i=2
while i<x//2:
    if(x%i==0):
        print("not prime")
        break
    i+=1
else: print("prime")

for i in range(2,x//2):
    if(x%i==0):
        print("not prime")
        break
else: print("prime")

for i in range(2,int(math.sqrt(x))+1):
    if(x%i==0):
        print("not Prime")
        break
else: print("prime")