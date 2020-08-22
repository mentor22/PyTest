""" def iseven(n):
    return n%2==0
neven=list(filter(iseven,nums)) """
import functools #or from functools import reduce

#f=lambda n:n%2==0

nums=[2,7,5,4,18,10]
#neven=list(filter(f,nums))

neven=list(filter(lambda n: n%2==0,nums))#filter values based on returned True/False to values passed to lambda/function.
print(neven)

doubles=list(map(lambda n: n*2,neven))#used when every value in sequence needs to be changed. Specially after filtering.
print(doubles)

#Now suppose I want to sum all the values of doubles, then we need to reduce the list to a single value using reduce.
#Can be used on a list mapped after filtering list, means filter the values then map it and then ultimstely reduce it
sum=functools.reduce(lambda a,b: a+b,doubles)#defined in functools module(function tools)
print(sum)