def fib(n):
    a=0
    b=1
    if(n<0):
        return
    elif(n==1):
        print(a)
    else:
        print(a)
        print(b)
    for i in range(2,n):
        c=a+b
        print(c)
        a=b
        b=c

fib(int(input("Enter number of sequence : ")))
print()

def fibupto(n):
    a=0
    b=1
    c=0
    if(n<0):
        return
    elif(n==1):
        print(a)
    else:
        print(a)
        print(b)
    for i in range(2,n):
        if(a+b>n):
            break
        else:
            c=a+b
            a=b
            b=c
            print(c)

fibupto(int(input("Enter maximum number in series : ")))