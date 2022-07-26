def sumofsquare(n):
    j=0
    for i in range(1,n+1):
        i=i*i
        j=j+i
    return j

print(sumofsquare(4))
