from array import *

def binary_search(key,arr,low,high):
    mid=(low+high)//2
    if low > high:
        return None 
    elif arr[mid]==key:
        return mid
    elif arr[mid]>key:
        return binary_search(key,arr,low,mid-1)
    else: return binary_search(key,arr,mid+1,high)

arr = array('i',[10,20,30,40,50,60,70,80])
key=int(input("Enter key to search : "))
index=binary_search(key,arr,0,len(arr)-1)
if(index!=None):
    print("Found at",index+1)    
else: print("Not Found")