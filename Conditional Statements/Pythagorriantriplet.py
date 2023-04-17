# Input three numbers and check if they are forming a Pythagorian Triplet

import math
a=int(input("Enter a number"))
b=int(input("Enter a number"))
c=int(input("Enter a number"))
if a**2 + b**2 == c**2:
    print("Pythagorian Triplet")
else:
    print("Not")
    
    