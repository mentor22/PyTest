i=1
while i<=4:
    print("Manoj ",end="")
    j=1
    while j<=4:
        print("rocks ",end="")
        j+=1
    i+=1
    print()
i=1
j=0
while i<=100:
    if i%3!=0 and i%5!=0:
        print(i,end=" ")
        j+=1
    i+=1
print(j)
i=0
while i<5:
    j=0
    while j<5:
        print("# ",end="")
        j+=1
    i+=1
    print()
i=0
while i<5:
    j=0
    while j<=i:
        print("# ",end="")
        j+=1
    i+=1
    print()
i=1
while i<5:
    j=i
    while j<=4:
        print(j,end=" ")
        j+=1
    i+=1
    print()
ch="ABCD"
ph="PQR"
for i in range(4):
    for j in range(i+1):
        print(ch[j],end=" ")
    k=i
    while k<3:
        print(ph[k],end=" ")
        k+=1
    print()