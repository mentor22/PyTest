def TopTen(): #generator function for in-built iterator
    yield 5 #return returns the value and end the function , this returns the object and doesnot end until last line

def TenSquares(): #Generator function to iterate for squares
    n = 1
    while n<=10: #will end for this condition only
        yield n*n
        n+=1 #important to iterate

val = TopTen()
print(val) #prints iterator object of val not value itself
print(val.__next__())
Squares = TenSquares()
for i in Squares:
    print(i)