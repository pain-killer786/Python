# Input x and y and perform |x|+x^y+sqrt(x)+cbrt(xy)+ceil(x+y)+floor(x-y)
import math
x=int(input("Enter a number"))
y=int(input("Enter a number"))
z = abs(x)+ math.pow(x,y)+ math.sqrt(x)+math.cbrt(x*y)+math.ceil(x+y)+math.floor(x-y)
print (z)

