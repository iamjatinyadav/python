"""
def armstrong(number):
    s=number
    totalval = len(str(number))
    val=0
    while number != 0 :
        r =number % 10
        val = val + (r**totalval)
        number = number//10
    if s == val:
        print(s,"is armstrong")
    else:
        print(s,"is not armstorng")
    

        



number=int(input("Enter the number:-"))

armstrong(number)

"""
#using recursion
"""
def armstoring(n):
    if n ==0:
        return 0
    else:
        return n%10 + armstoring((n-1)//10)

print(armstoring(153))

"""