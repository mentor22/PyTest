import array
import numpy
vals = array.array('i',[10,20,30,40,50])
for i in range(2,4):
    vals[i]=vals[i+1]
print(vals)
sliced_arr=vals[:4]
print(sliced_arr)
i=0
j=len(vals)-1
while i<j:
    vals[i],vals[j]=vals[j],vals[i]
    i+=1
    j-=1
print(vals)
vals = numpy.array([10,20,30,40,50],int)
print(vals)