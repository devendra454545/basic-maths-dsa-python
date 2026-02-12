def gcd(n1, n2):
    n1 = abs(n1)
    n2 = abs(n2)

    for i in range(min(n1, n2), 0, -1):
        if n1 % i == 0 and n2 % i == 0:
            return i
    return 1

print(gcd(12, 8)) 