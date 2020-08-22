def person(name,*data): #variable length argument(VLA)
    print(name)
    print(data)

def person1(name,**data): #keyword variable length argument(KVLA)
    print(name)
    print(data)

def person2(name,**data): #keyword variable length argument(KVLA)
    print(name)
    for i,j in data.items(): #contains keyword and argument value
        print(i,":",j)

person("Manoj",22,"Lucknow",707121)
person1("Manoj",age=22,city="Lucknow",mob=707121)
person2("Manoj",age=22,city="Lucknow",mob=707121)