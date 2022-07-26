"""
#using recursion

def fibo(n):
    if n in [0,1]:
        return n
    else:
        return fibo(n-1)+ fibo(n-2)

print(fibo(9))


"""
#using iterations


def fibo(n):
    a=0
    b=1
    if n==0:
        print(a)
    elif n==1:
        print(b)
    else:
        for i in range(1,n):
            c=a+b
            a=b
            b=c
        print(c)

fibo(10)
    