# Input three sides of a triangle and find the type of triangle

h=int(input("Enter a side"))
b=int(input("Enter a side"))
p=int(input("Enter a side"))
if h==b==p:
    print("Equilateral Triangle")
elif h==b!=p:
    print("Isoceles Triangle")
else:
    print("Scalene Triangle")