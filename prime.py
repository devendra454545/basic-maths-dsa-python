def checkPrime(n):
    count = 0  

    for i in range(1, n + 1):
       
        if n % i == 0:
            count += 1  
    return count == 2

n = 7  
isPrime = checkPrime(n)  

if isPrime:
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")