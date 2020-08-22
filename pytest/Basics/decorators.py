def div(a,b):
    print(a/b)

print("Before change : ")
div(2,4)

#we want to swap numerator with denominator when first smaller than later,
#but without changing or touching div function.
#Decorators in python changes working of a function without touching the function itself as its a funtional language

def smart_div(func):

    def inner(a,b): #parameter names can be different, inner(name be changed) function points to the same div function
        if(a<b):
            a,b=b,a
        return func(a,b)
    return inner #returns the function with changed working

div = smart_div(div)
print("After change : ")
div(2,4)

div1 = smart_div(div)
div1(4,12)

smart_div(div(2,4)) #can also be called in this manner with assigning to any function