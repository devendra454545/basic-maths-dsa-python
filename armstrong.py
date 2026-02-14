def armstrong(n):
    temp = n
    total = 0
    length = len(str(n))

    while n>0:
        digit = n%10
        total = total + digit**length
        n = n//10
    return total == temp

print(armstrong(153)) # tells that a number is armstrong or not


# code to print all armstrong numbers and count of them
count=0
for i in range(1,1001): #to print all armstrong numbers from 1 to 1000
    if(armstrong(i)):
        print(f"{i} is armstrong")
        count +=1
print(count) #prints number of armstrong numbers

# Complexity Analysis
# Time Complexity: O(log10N + 1) where N is the input number. The time complexity is determined by the number of digits in the input integer N. In the worst case when N is a multiple of 10 the number of digits in N is log10 N + 1.

# Space Complexity: O(1) as only a constant amount of additional memory for the reversed number regardless of size of the input number.