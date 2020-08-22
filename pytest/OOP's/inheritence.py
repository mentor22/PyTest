class A:
    def __init__(self):
        print("in init A")

    def feature1(self):
        print("Feature 1 is working")

    def feature2(self):
        print("Feature 2 is working")

class B(A): #single level inheritence

    def feature3(self):
        print("Feature 3 is working")

    def feature4(self):
        print("Feature 4 is working")

class C(B): #multilevel inheritence
    def feature5(self):
        print("Feature 5 is working")

class D():
    def feature1(self):
        print("Feature 6(1) is working")

class multiple(A,D):
    def __init__(self):
        super().__init__() #Method Resolution order i.e. A is inherited first(left one) as multiple 
                            #then super() will be biased on A, even super() method will work in same fashion
        print("in init multiple")

    def feature7(self):
        super().feature1() #will be biased towards feature 1 of A class as its in left
        print("Feature 7 is working")

c = C() 
c.feature1()
c.feature3()
c.feature5()
mul = multiple()
mul.feature2()
mul.feature1()
mul.feature7()