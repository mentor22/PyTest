class TopTen: #self iterator
    def __init__(self): #sets initial value 
        self.num=1

    def __iter__(self): #returns the object of iterator
        return self

    def __next__(self):
        if self.num<=10:
            val = self.num
            self.num+=1
            return val
        else: raise StopIteration

values = TopTen()
print(values) #gives object of iterator TopTen
print(values.__next__()) #1 #returns the current value of self.num(or num) in iterator object
print(next(values)) #2 #inbuilt function to print next value in object, __next__ is also inbuilt for iterators like for
for i in values: #returns the current value upto the end of values or upto we code it to go, can go to infinite too
    print(i) #3 4 5 6 7 8 9 10