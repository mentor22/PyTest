import math
x=["Manoj",22,11]
for i in x:
    print(i)
x="MANOJ"
for i in x:
    print(i)
for i in ["Manoj",22,11]:
    print(i)
for i in range(1,23):
    print(i,end=" ")
print()
for i in range(1,23,3):
    print(i,end=" ")
print()
for i in range(22,0,-1):
    print(i,end=" ")
print()
for i in range(22,0,-2):
    print(i,end=" ")
print()
for i in range(10):
    print(i,end=" ")
print()
i=1
while i<=500:
    if(math.floor(math.sqrt(i))==math.sqrt(i)):
        print(i,end=" ")
    i+=1
print()