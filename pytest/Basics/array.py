import array
from array import *
vals = array('i',[2,8,-9,20,22])
#vals.reverse()
vals.append(6)
vals.remove(20)
print(vals)
print(vals[0])
for i in vals:
    print(i,end=" ")
print()
for i in range(len(vals)):
    print(vals[i],end=" ")
print()
newArr=array(vals.typecode,(a for a in vals))
for i in newArr:
    print(i,end=" ")
print()
"""vals=array('u',['a','b','c'])
for i in vals:
    print(i,end=" ")
print()
 """
for i in range(len(vals)-1):
    for j in range(i+1,len(vals)):
        if(vals[i]>vals[j]):
            vals[i],vals[j]=vals[j],vals[i]
for i in range(len(vals)):
    print(vals[i],end=" ")
print()
x=int(input("Enter a number : "))
fact=1
while x>0:
    fact*=x
    x-=1
print(fact)
newArr=array('i',[])
x=int(input("Enter length of array : "))
print("Enter ",x," elements")
for i in range(x):
    newArr.append(int(input()))#in empty array we can't directly insert the value
for i in newArr:
    print(i,end=" ")
print()
y=int(input("Enter value to search : "))
for i in range(x):
    if(newArr[i]==y):
        print(y," is found at index : ",i)
        break
print(newArr.index(y))
newArr.remove(newArr[2])
print(newArr)