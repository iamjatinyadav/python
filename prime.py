def checkprime(n):
    for i in range(2,int(n//2)+1):
        if n%i == 0:
            print(n,"number is not prime")
            break
    else:
        print(n,"number is prime")

checkprime(12)