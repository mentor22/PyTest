def prof(name,age=20):
    print(name)
    print(age)

def sum(a,*b):
    c=a
    for i in b:
        c=c+i
    print("Sum =",c)

def sum1(*b):
    c=0
    for i in b:
        c=c+i
    print("Sum =",c)

prof("Manoj",22)#position
prof(age=22,name="Manoj")#keyword
prof("Manoj")#default
sum(11,5,8,7)#variable length
sum1(11,5,8,7)#variable length
print("END")