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