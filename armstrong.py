def armstrong(n):
    temp = n
    total = 0
    length = len(str(n))

    while n>0:
        digit = n%10
        total = total + digit**length
        n = n//10
    return total == temp

print(armstrong(153))

count=0
for i in range(1,1001):
    if(armstrong(i)):
        print(f"{i} is armstrong")
        count +=1
print(count)