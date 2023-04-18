# Find the sum and product of squares of all the numbers from 1 to n
import math
n=int(input("Enter a number"))
s=0;p=1
i=1
while(i<=n):
    s=s+math.pow(i,2)
    p=p*math.pow(i,2)
    i+=1
print(s,end=" ")
print(p)
    