def revNum(n):
    rev = 0
    
    if n < 0:
        sign = -1 
    else:
        sign = 1
    n = abs(n)
    while n > 0:
        lastDigit = n%10            
        rev = rev * 10 + lastDigit  
        n = n//10                   
    return sign * rev
print(revNum(-122))