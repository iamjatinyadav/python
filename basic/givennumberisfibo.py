
import math


def issquare(x):
    c = int(math.sqrt(x))
    return c*c == x

def isfibonacci(n):
    return issquare(5*n*n+4) or issquare(5*n*n-4)


for i in range(1,10):
    if isfibonacci(i) == True:
        print(i,"number is fibo")
    else:
        print(i,"number is not fibo")