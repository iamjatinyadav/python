from array import *

arr=array('i',[10,20,45,35,2,78,4,100,67,89])
d=2
n=10


"""
# using list slicing
#space_complexity=O(1)
#time_complexity=O(1)

def rotatelist(arr,d,n):
    arr[:]=arr[d:n]+arr[0:d]
    return arr

print(rotatelist(arr,d,n))


"""

#using temp array
#space_complexity=O(1)
#time_complexity=O(1)





def arrrotations(arr,d,n):
    temp=array('i',[])
    for i in range(n):
        if i<d:
            temp.append(arr[i])
    for i in temp:
        arr.remove(i)
        arr.append(i)
    
    return arr

print(arrrotations(arr,d,n))        



