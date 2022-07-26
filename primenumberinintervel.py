def findprime(start,end):
    for i in range(start,end+1):
        for j in range(2,int(i//2)+1):
            if i%j == 0:
                break
        else:
            print(i,"is prime")
            
findprime(1,50)