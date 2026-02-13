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

# Complexity Analysis

# Time Complexity: O(N), as we iterate from 1 to N performing constant-time operation for each iteration.

# Space Complexity : O(1), as the space used by the algorithm does not increase with the size of the input.