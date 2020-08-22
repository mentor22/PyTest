import sys

sys.setrecursionlimit(1000) #for increasing recursion limit
print(sys.getrecursionlimit()) #for printing updated recursion limit

def fact(n):
    if n==0:
        return 1
    elif n>0:
        return n*fact(n-1)

print(fact(int(input("Enter a number : "))))