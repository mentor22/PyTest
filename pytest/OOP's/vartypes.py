class car:
    wheels=4 #class/static variable defined outside function
    def __init__(self):
        self.mile=8 #instance variable defined inside __init__
        self.company='Audi' #instance variable defined inside __init__

c1=car()
c2=car()

car.mile=18
c1.mile=10
c2.wheels=40
car.wheels=20

print(c1.company,c1.mile,c1.wheels)
print(c2.company,c2.mile,c2.wheels)