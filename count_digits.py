def count_digits(n):
    if n == 0:
        return 1
    n = abs(n)
    count = 0
    while n>0:
        count = count+1
        n = n // 10
    return count

print (count_digits(-6666))
print (count_digits(0))
print (count_digits(16))