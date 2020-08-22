from numpy import *

vals = array([10,20,30,40,50])
print(vals.dtype)
print(vals)

vals=linspace(0,16) #breaks down the range by default into 50 parts
print(vals)
vals = linspace(0,15,16)#breaks down the range into 16 parts
print(vals)
vals = linspace(0,15,10)#breaks down the range into 10 parts
print(vals)
vals = linspace(0,15,20)
print(vals)
vals = arange(1,15,3)#builds an array within range 1,15 starting with 1 and leaving 2 intermediate elements ex: 1,4,7
print(vals)
vals = logspace(1,40,5)#takes 10^1 to 10^40 and breaks into 5 parts, parts decided by log
print(vals)
print("%.2f"%vals[0]," %.2f"%vals[3])
vals = zeros(5)#create an array of 5 zeroes in default float data type
print(vals)
vals = ones(5)#create an array of 5 ones in default float data type
print(vals)
vals = ones(5,int)#specify data type as integer
print(vals)