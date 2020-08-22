class First:
    def method1(self):
        print("Welcome to Method 1 :","Manoj Moolchandani")
        print("I have a system with",self.cpu ,"and",self.ram)

    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram

    def compare(self,other):
        if(self.ram==other.ram):
            return True
        else: return False
        
met=First('i5',8)
print(id(met))
met1=First('Ryzen 3',16)
print(id(met1))

""" First.method1(met) #not so preferred but one method to call a method of a class
First.method1(met1) """

if(met.compare(met1)):
    print("Same")
else: print("Different")

met.method1() #takes met as argument automatically
met1.method1() #takes met1 as argument automatically