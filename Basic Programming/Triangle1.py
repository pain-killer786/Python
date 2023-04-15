# Input the dimensions of a triangle and find Area

import math
a=int(input("Enter a side"))
b=int(input("Enter a side"))
c=int(input("Enter a side"))
s=(a+b+c)/2
A=math.sqrt(s*(s-a)*(s-b)*(s-c))
print(A)
