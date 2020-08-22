class overload:
    def sum(self,a=None,b=None,c=None): #indirect method overloading, direct overloading not supported in python
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else: s=a
        return s

s = overload()
print(s.sum(5,8)) #method overloading
print(s.sum(3,4,5))
print(s.sum(9))