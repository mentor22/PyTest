a=10
print(id(a))

def global1():
    a=8
    x=globals()['a']
    print(id(x),"x :",x)
    print("in fun a :",a)
    globals()['a']=15
    
global1()
print("outside fun a:",a)