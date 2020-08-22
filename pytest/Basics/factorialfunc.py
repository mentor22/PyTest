def fact(n):
    f=1
    for i in range(2,n+1):
        f*=i
    return f

factorial=fact(int(input("Enter a number : ")))
print(factorial)