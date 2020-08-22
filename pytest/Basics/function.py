def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d

def update(x):
    print(id(x))#points to same object containing 10 which x outside the function waas pointing
    x=8
    print(id(x)," x : ",x)#points to an object containing 8 as value, different from x outside the function

def update1(lst):
    print(id(lst))#points to same lst outside the function
    lst[1]=25
    print(id(lst),"lst :",lst)#still points to same lst outside the function

x=int(input("Enter 2 numbers :"))
y=int(input())
result1,result2=add_sub(x,y)
print(result1,result2)
print(id(x))
update(x)
print("x : ",x)#value won't change
lst=[10,20,30]#mutable object
print(id(lst))
update1(lst)