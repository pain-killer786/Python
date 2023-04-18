# Find the sum and product of all the numbers from 1 to n
n=int(input("Enter a number"))
s=0;p=1
i=1
while(i<=n):
    s=s+i
    p=p*i
    i+=1
print(s, end=" ")
print(p)
    