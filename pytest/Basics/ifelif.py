x=int(input("Enter a number"))
y=int(input("Enter 2nd number"))
z=int(input("Enter 3rd number"))
if x==1:
    print("One")
elif x==2:
    print("Two")
elif x==3:
    print("Three")
else: print("Wrong Input")
if x>y and x>z:
    print(x,"is greater")
elif y>z:
    print(y,"is greater")
else: print(z,"is greater")