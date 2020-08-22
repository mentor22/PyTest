class Student:
    def __init__(self,name,rollno,brand,cpu,ram):
        self.name=name
        self.rollno=rollno
        self.lap=self.laptop(brand,cpu,ram) #inner class object can be created outside class also using name of class

    def show(self):
        print(self.name,self.rollno)
        self.lap.show()

    class laptop:
        def __init__(self,brand,cpu,ram):
            self.brand=brand
            self.cpu=cpu
            self.ram=ram

        def show(self):
            print(self.brand,self.cpu,self.ram)

s1 = Student("Manoj",51910017,'lenevo','i3',4)
s1.show() #show of Student outer class

lap=Student.laptop('lenevo','i3',4) #creating object of inner class inside as well as outside too
lap.show() #show of laptop inner class