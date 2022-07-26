from array import *

arr=array('i',[10,20,45,35,2,78,4,100,67,89])
def findlargestarray(array):
    val=0
    for i in array:
        if val <= i:
            val=i
    return val

findlargestarray(arr)
    