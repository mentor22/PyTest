from numpy import *

arr=array([1,2,3,4,5])
""" print(arr+5)
arr=arr+5#add 5 to each element of the array
print(arr)
arr2=array([6,9,7,3,2])
print(arr2)
arr3=arr+arr2
print(arr3)
print(log(arr))
print(sqrt(arr))
print(sin(arr))
print(sum(arr))
print(min(arr))
print(sort(arr2))
print(concatenate([arr,arr2])) """
arr3=arr#will not create a new array, both will point to same memory of the array itself
print(arr)
print(arr3)
print(id(arr),id(arr3))
arr2=arr.view()#helps in creating acopy but new array yet it's a shallow copy 
arr[2]=7#will be reflected in both as it's shallow copy
print(arr)
print(arr2)
print(id(arr),id(arr2))
arr2=arr.copy()#helps in creating acopy but new array and it's a deep copy 
arr[2]=6#will be reflected in arr only
print(arr)
print(arr2)
print(id(arr),id(arr2))