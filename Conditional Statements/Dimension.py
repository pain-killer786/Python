# Input dimensions and find the area of circle, traingle, rectangle depending on user choice

print("1. Area of Circle 2. Area of Triangle 3.Area of Rectangle")
a= int(input("Enter Your Choice"))
if a==1:
    r=int(input("Enter radius"))
    print(3.14*r*r)
elif a==2:
    b=int(input("Enter base"))
    h=int(input("Enter height"))
    print(0.5*b*h)
elif a==3:
    b=int(input("Enter length"))
    l=int(input("Enter breadth"))
    print(l*b)
else:
    print("Wrong choice")
    