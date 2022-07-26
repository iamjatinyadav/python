def sumofsquare(n):
    j=0
    for i in range(1,n+1):
        i=i**3
        j=j+i
    return j

print(sumofsquare(5))