def count_five(lst):
    c=0
    for i in lst:
        if(len(i)>5):
            c+=1
    return c



print("Enter 10 names of variable length")
lst=[]
for i in range(10):
    lst.append(input())
print("Names greater than length 5 : {}".format(count_five(lst)))
