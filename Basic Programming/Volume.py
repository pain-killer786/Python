# Input the dimensions of a cuboid, sphere, cube, cylinder and find their volume 

import math
a=int(input("Enter side"))
V1=math.pow(a,3)
r=int(input("Enter Side"))
V2=(4/3)*(22/7)*(math.pow(r,3))
b=int(input("Enter side"))
c=int(input("Enter side"))
d=int(input("Enter side"))
V3=b*c*d
l=int(input("Enter side"))
V4=(1/3)*(22/7)*(math.pow(l,3))
print(V1,V2,V3,V4)