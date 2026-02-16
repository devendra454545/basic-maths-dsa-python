def divisors(n):
    res = []
    for i in range(1,n+1):
        if(n%i==0):
            res.append(i)
    return res
print(*divisors(36))


# Time Complexity

# The loop runs from 1 to n, so it iterates n times → O(n).

# Inside the loop, the operation n % i is constant time, O(1).

# Appending to a list is also amortized O(1).

# So the overall time complexity is:
# O(n)
# 	​

# 2. Space Complexity

# The list res stores all divisors of n.

# In the worst case (for n being a highly composite number like 36), the number of divisors is at most n (actually, the number of divisors is O(n^(1/2)) on average, but let's consider worst case as O(n)).

# Apart from res, we only use a loop variable i → negligible.

# So the space complexity is:
# O(n)