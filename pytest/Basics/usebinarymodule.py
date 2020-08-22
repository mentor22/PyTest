import Modules.binarysearch as md
from array import *
arr = array('i',[])
n=int(input('Enter size of list'))
for i in range(n):
    arr.append(int(input()))
index=md.binary_search(int(input("Enter key to search")),arr,0,len(arr)-1)
if(index!=None):
    print("Found at",index)
else: print("Not found")
