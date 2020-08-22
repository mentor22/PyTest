class Student:
    school="Avadh Collegiate"
    def __init__(self,m1,m2,m3): #self constructor
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def average(self): #instance method
        return (self.m1+self.m2+self.m3)/3

    def get_m1(self): #accessor method to access/get an instance value
        return self.m1

    def set_m1(self,value): #mutator method to change/mutate an instance value
        self.m1=value

    @classmethod #has to do with class variable only
    def getschool(cls):
        print(cls.school)

    @staticmethod
    def fact(n): #has nothing to do with instance variable as well as class variable
        f=1
        for i in range(2,n+1):
            f*=i
        return f

s1 = Student(23,46,34)
print(s1.average())
s1.set_m1(10)
print("m1 = {}".format(s1.get_m1()))
print("School",Student.getschool())
factresult=s1.fact(int(input("Enter a number : ")))
print("Factorial :",factresult)